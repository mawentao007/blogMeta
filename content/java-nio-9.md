Title: Java NIO-9  SocketChannel
Date: 2015-9-15 
Category: 技术文章
Tags:NIO,教程,JAVA
Summary:Java NIO 文件通道是用来连接文件的通道。通过文件通道可以对文件进行读写操作。Java NIO文件通道是Java IO API之外的读写文件的另一个选择。

<a href=http://tutorials.jenkov.com/java-nio/socketchannel.html>原文链接</a>

Java NIO SocketChannel用来连接TCP网络的套接字，功能类似于Java Networking‘s Sockets。创建SocketChannel的方法有两种：

+	打开SocketChannel并且连接到网络上的服务器
+	连接请求到达ServerSocketChannel的时候被创建


<h4>&#9734;&nbsp;打开/关闭SocketChannel</h4>


	//打开SocketChannel
	SocketChannel socketChannel = SocketChannel.open();
	socketChannel.connect(new InetSocketAddress("http://jenkov.com", 80));
    
    //关闭SocketChannel
    socketChannel.close();   


<h4>&#9734;&nbsp;读取SocketChannel</h4>

读取SocketChannel中的数据需要调用一种*read()*方法：

	ByteBuffer buf = ByteBuffer.allocate(48);

	int bytesRead = ocketChannel.read(buf);
    
首先分配一个缓冲区，从SocketChannel中将数据读入该缓冲区。之后调用*SocketChannel.read()*方法进行读取。该方法从文件通道中将数据读入缓冲区。返回值表示写入缓冲区的字节数。如果返回-1，说明到达了文件结尾。

<h4>&#9734;&nbsp;将数据写入SocketChannel</h4>

将数据写入SocketChannel要利用到*SocketChannel.write()*方法，该方法需要一个Buffer作为参数，如下：

```
String newData = "New String to write to file..." + System.currentTimeMillis();

ByteBuffer buf = ByteBuffer.allocate(48);
buf.clear();
buf.put(newData.getBytes());

buf.flip();

while(buf.hasRemaining()) {
    channel.write(buf);
}

```

注意while循环中*SocketChannel.write()*的调用方式。因为*write()*方法写入SocketChannel的字节数无法确定，因此需要重复调用*write()*方法直到Buffer中没有可以进行写入的数据。

<h4>&#9734;&nbsp;非阻塞模式</h4>

SocketChannel可以被设置为非阻塞模式，*connect()*,*read()*,*write()*在此模式下都处于异步模式。

**连接**

在非阻塞模式下调用*connect()*方法，方法可以在连接建立之前就返回。为了确定连接是否建立，需要调用*finishConnect()*方法，eg.

```
socketChannel.configureBlocking(false);
socketChannel.connect(new InetSocketAddress("http://jenkov.com", 80));

while(! socketChannel.finishConnect() ){
    //wait, or do something else...    
}
```

**write()**

在非阻塞模式下的*write()*方法可能在未写入任何值的情况下返回，因此需要循环调用*write()*方法。但是上文的实例已经这么处理了，因此这里无需修改。（译者：为什么异步模式下不尝试利用回调或者future？）

**read()**

在非阻塞模式下*read()*方法返回的时候可能未读取任何值，要注意通过返回的int值来确认读取的数据量。

**非阻塞模式和选择器**

非阻塞模式和选择器协同工作的效果很好。通过将若干SocketChannel注册到选择器，用户可以通过询问选择器获知读写就绪的通道。













