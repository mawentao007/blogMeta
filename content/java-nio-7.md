Title: Java NIO-7 选择器
Date: 2015-8-10 
Category: 技术文章
Tags:NIO,教程,JAVA

选择器(selector)是Java NIO中的重要组件，负责监控一个或者多个通道的状态，并且决定相关通道是否准备好读写操作。通过这种方式，一个线程可以管理多个通道，也就是管理多个网络连接。
<hr>

<h4>&#9734;&nbsp;为什么使用选择器</h4>

利用单个线程监控多个通道的好处之一就是可以节约线程。事实上，用户甚至可以用一个线程监控所有通道。因为线程的切换对于操作系统来讲代价比较昂贵，线程同时也会消耗一部分系统资源，因此在满足需求的情况下，对于线程的使用原则是越少越好。

现代的CPU和操作系统处理多任务的能力越来越强，因此多线程带来的副作用大幅减少。事实上，如果CPU有多个核，那么不使用多任务并行是对CPU资源的一种浪费。当然这不是我们要讨论的主要内容。

下图表示一个选择器监控三个通道：

<p align="center">
	<img class=embeded-img src="./images/overview-selectors.png">
</p>

<hr>

<h4>&#9734;&nbsp;创建选择器</h4>


	Selector selector = Selector.open();

<hr>

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
    
<hr>
<h4>&#9734;&nbsp;选择关键字</h4>

	

<hr>

<h4>&#9734;&nbsp;通过选择器选择通道</h4>


<hr>

<h4>&#9734;&nbsp;唤醒</h4>


<hr>
<h4>&#9734;&nbsp;关闭</h4>


<hr>

<h4>&#9734;&nbsp;完整事例</h4>


<hr>