Title: Java NIO-7 选择器
Date: 2015-8-10 
Category: 技术文章
Tags:NIO,教程,JAVA

<a href=http://tutorials.jenkov.com/java-nio/selectors.html>原文链接</a>

选择器(selector)是Java NIO中的重要组件，负责监控一个或者多个通道的状态，并且决定相关通道是否准备好读写操作。通过这种方式，一个线程可以管理多个通道，也就是管理多个网络连接。

<h4>&#9734;&nbsp;为什么使用选择器</h4>

利用单个线程监控多个通道的好处之一就是可以节约线程。事实上，用户甚至可以用一个线程监控所有通道。因为线程的切换对于操作系统来讲代价比较昂贵，线程同时也会消耗一部分系统资源，因此在满足需求的情况下，对于线程的使用原则是越少越好。

现代的CPU和操作系统处理多任务的能力越来越强，因此多线程带来的副作用大幅减少。事实上，如果CPU有多个核，那么不使用多任务并行是对CPU资源的一种浪费。当然这不是我们要讨论的主要内容。

下图表示一个选择器监控三个通道：

<p align="center">
	<img class=embeded-img src="./images/overview-selectors.png">
</p>


<h4>&#9734;&nbsp;创建选择器</h4>


	Selector selector = Selector.open();


<h4>&#9734;&nbsp;将通道注册到选择器</h4>

必须先将通道注册到选择器上才可以实现选择器对该通道的监控，注册方法如下：

	channel.configureBlocking(false);

	SelectionKey key = channel.register(selector, SelectionKey.OP_READ);
    
如果利用选择器，那么通道必须是非阻塞模式。这意味着不可以将FileChannel和选择器一同使用，因为FileChannel不能切换到非阻塞模式。

注意register()方法的参数，表示可以由选择器监控的通道事件，有如下四种：

+	Connect
+	Accept
+	Read
+	Write	

一个通道触发一个事件，我们就说这个事件已经准备好了。因此一个通道成功连接到另外一台服务器，就被称为“连接成功”。如下是四个通道事件：

+	SelectionKey.OP_CONNECT
+	SelectionKey.OP_ACCEPT
+	SelectionKey.OP_READ
+	SelectionKey.OP_WRITE

如果用户对多个事件感兴趣，可以使用OR：

	int interestSet = SelectionKey.OP_READ | SelectionKey.OP_WRITE; 
    
<h4>&#9734;&nbsp;选择关键字</h4>

正如前面所介绍的，当用户利用register()注册通道到选择器，姜宏返回一个SelectionKey对象。这个SelectionKey对象包含一系列有意思的属性：

+	The interest set
+	The ready set
+	The Channel
+	The Selector
+	An attached object (optional)

下面将会介绍这些属性。

**Interest Set**

这个集合包含一系列“选择”过程中的事件，用户可以通过SelectionKey来读写这个集合。
```
int interestSet = selectionKey.interestOps();

boolean isInterestedInAccept  = interestSet & SelectionKey.OP_ACCEPT;
boolean isInterestedInConnect = interestSet & SelectionKey.OP_CONNECT;
boolean isInterestedInRead    = interestSet & SelectionKey.OP_READ;
boolean isInterestedInWrite   = interestSet & SelectionKey.OP_WRITE; 
```
可以通过"&"符号近线筛选来找出集合中的事件。

**Ready Set**

这个集合包含通道已经就绪的事件，用户可以通过selection操作来获取这个事件集合：

	int readySet = selectionKey.readyOps();
    
除了之前介绍的测试事件的AND方法，也可以通过如下的方法测试，返回一个布尔值:

```
selectionKey.isAcceptable();
selectionKey.isConnectable();
selectionKey.isReadable();
selectionKey.isWritable();
```

**Channel + Selector**
通过SelectionKey访问channel + selector很容易，如下：
	
    Channel  channel  = selectionKey.channel();
	Selector selector = selectionKey.selector(); 

**Attaching Objects**

用户可以通过将一个对象附着到一个SelectionKey来识别通道，或者添加更多信息到通道。例如，用户可以将channel和对应的buffer组合到一起，或者和一个集成更多信息的对象组合：

	selectionKey.attach(theObject);

	Object attachedObj = selectionKey.attachment();
    
也可以在注册Channel到Selector时将要附着的对象作为参数传递给register()：
	
    SelectionKey key = channel.register(selector, SelectionKey.OP_READ, theObject);
    

<h4>&#9734;&nbsp;通过选择器选择通道</h4>

注册一个或者多个channel到selector之后就可以调用一种select()方法，这些方法用来返回已经触发并且用户感兴趣的事件所对应的通道（connect,accept,read or write)。如下有几种select()方法：

+	int select()
+	int select(long timeout)
+	int selectNow()

*select()* 阻塞，直到一个通道触发一个注册过的事件；

*select(long timeout)*,基本同上，有一个等待时长；

*selectNow()*非阻塞，立刻返回。

select()方法返回的int值表示已经就绪的channel个数，也就是两次调用select()之间就绪的通道个数。如果用户调用select(),返回1因为有一个channel就绪，这时再次调用select()，又有一个channel就绪，这时返回的还是1。如果这时没有处理第一个就绪的channel，那么这时候有两个channel都就绪。

*selectedKeys()*

一旦用户唤醒其中一个select()方法，返回值预示着一个或者多个channels已经准备好了，用户可以通过“selected key set”访问这些channel。访问的方法是调用selectedKeys()，如下：

	Set<SelectionKey> selectedKeys = selector.selectedKeys(); 
    
当用户通过Channel.register()将channel注册到selector，该方法返回一个SelectionKey对象。这个key表示相关通道已经注册到了某个selector。用户通过selectedKeySet()方法访问的就是这些key。

可以通过迭代器访问这些已经准备好的channel：
```
Set<SelectionKey> selectedKeys = selector.selectedKeys();

Iterator<SelectionKey> keyIterator = selectedKeys.iterator();

while(keyIterator.hasNext()) {
    
    SelectionKey key = keyIterator.next();

    if(key.isAcceptable()) {
        // a connection was accepted by a ServerSocketChannel.

    } else if (key.isConnectable()) {
        // a connection was established with a remote server.

    } else if (key.isReadable()) {
        // a channel is ready for reading

    } else if (key.isWritable()) {
        // a channel is ready for writing
    }

    keyIterator.remove();
}
```

这个循环迭代访问selected key set中的keys。对于每个key，测试相关事件是否有通道已经就绪。

注意keyIterator.remove()调用。Selector不会主动移出SelectionKey实例，需要用户在处理完channel之后手动移出。下一次通道就绪，选择器会再次将响应的key加入到selected key set。

channel通过SelectionKey.channel()方法返回，这个channel就是要处理的channel。

<h4>&#9734;&nbsp;唤醒</h4>

调用select()方法的线程被阻塞，不过利用Selector.wakeup()方法，即使没有channel准备就绪，也可以使其脱离阻塞状态。不过该方法需要通过另一个线程进行调用，调用之后被阻塞的线程会立刻返回。

如果没有线程被阻塞，也就是没有唤醒任何线程，那么下一个调用select()的线程会被立刻唤醒。


<h4>&#9734;&nbsp;关闭</h4>

调用Selector.close()方法可以立刻关闭Selector，该方法会使所有注册到相应Selector的SelectionKey实例失效，但是channel不会被关闭。



<h4>&#9734;&nbsp;完整示例</h4>

```
Selector selector = Selector.open();

channel.configureBlocking(false);

SelectionKey key = channel.register(selector, SelectionKey.OP_READ);

while(true) {

  int readyChannels = selector.select();

  if(readyChannels == 0) continue;

  Set<SelectionKey> selectedKeys = selector.selectedKeys();

  Iterator<SelectionKey> keyIterator = selectedKeys.iterator();

  while(keyIterator.hasNext()) {

    SelectionKey key = keyIterator.next();

    if(key.isAcceptable()) {
        // a connection was accepted by a ServerSocketChannel.

    } else if (key.isConnectable()) {
        // a connection was established with a remote server.

    } else if (key.isReadable()) {
        // a channel is ready for reading

    } else if (key.isWritable()) {
        // a channel is ready for writing
    }

    keyIterator.remove();
  }
}
```



