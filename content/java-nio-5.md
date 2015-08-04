Title: Java NIO-5 分发器/收集器
Date: 2015-8-3 
Category: 技术文章
Tags:NIO,教程,JAVA

Java NIO内置支持分发器(scatter)/收集器(gather)。分发器/收集器在读写通道的时候使用。

分发器的读取操作是指从一个通道读取数据到一个或者多个缓冲区。这个操作可以被认为是通道将数据“分发”到多个缓冲区。

收集器的写操作是指将数据从一个或者多个缓冲区写入单个通道。这个操作可以视作从多个缓冲区“收集”数据到一个通道。

在用户需要利用多个分别传输数据的组件进行工作的时候，分发/收集操作就变得格外有意义。例如，如果一个消息包含头部和内容，用户可能需要将这两部分保存在不同的缓冲区中。有了收集分发机制可以使用户更好的处理这种分别存储的状况。

####分发读

一个"分发读"操作将数据从一个通道读入多个缓冲区。如下图：
<p align="center">
	<img class=embeded-img src="./images/scatter.png">
</p>
<p align="center">
**JAVA NIO:分发读操作**
</p>

如下是一个分发读操作的示例代码：

	ByteBuffer header = ByteBuffer.allocate(128);
	ByteBuffer body   = ByteBuffer.allocate(1024);

	ByteBuffer[] bufferArray = { header, body };

	channel.read(buffers);
    
注意首先将缓冲区放入一个队列，之后再将这个队列作为参数传递给*channel.read()*方法。这个方法将会从通道中读取数据，并依次放入队列包含的缓冲区中。一旦一个缓冲区被填满，通道将数据写入下一个缓冲区。

由于数据是一个个填满缓冲区的，因此这种方法不适用于动态消息大小。换句话说，如果用户的消息包含头部和内容，那么头部的大小必须固定下来，分发器才能正常工作。

####收集写

"收集写"是将数据从多个缓冲区读出并写入一个通道。如图：
<p align="center">
	<img class=embeded-img src="./images/gather.png">
</p>
<p align="center">
**JAVA NIO:收集写**
</p>
如下是示例代码：
	
    ByteBuffer header = ByteBuffer.allocate(128);
	ByteBuffer body   = ByteBuffer.allocate(1024);

	//write data into buffers

	ByteBuffer[] bufferArray = { header, body };

	channel.write(buffers);
缓冲区队列作为参数传递给*write()*方法，这个方法按顺序将缓冲区的数据写入通道。只有position和limit之间的数据会被写入。因此，收集写可以应对动态消息大小的情况，这点与分发读不同。