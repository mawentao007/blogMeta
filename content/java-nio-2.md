Title: Java NIO-2 概述
Date: 2015-7-29 
Category: 技术文章
Tags:NIO,教程,JAVA

Java NIO包含如下核心组件：
+ 通道
+ 缓冲区
+ 选择器

Java NIO除了这写还有很多类和组件，但是我认为这三者是API的核心。其它组件，例如管道（Pipe）和文件锁（FileLock）等仅仅是辅助联结这三个核心组件进行工作的工具类。因此，我将会在本章重点讲这三个组件。其它组件将会在其它章节涉及。
####通道和缓冲区
所有的IO和NIO都是由通道开始。一个通道就像一个流。数据可以从通道读入缓冲区，也可以由缓冲区写入通道。下图是一个简单描述：

![1](http://scalaboy.top/blogPicture/overview-channels-buffers.png)

**&ensp;&ensp;Java NIO：通道读数据到缓冲区，缓冲区写数据到通道**

通道和缓冲区有很多类型。如下列举了Java NIO实现的一些初级通道类型：
+ FileChannel
+ DatagramChannel
+ SocketChannel
+ ServerSocketChannel

不难看出，这些通道的类型覆盖了UDP+TCP网络IO，还有文件IO
如下是Java NIO中实现的核心缓冲区的列表：
+ ByteBuffer
+ CharBuffer
+ DoubleBuffer
+ FloatBuffer
+ IntBuffer
+ LongBuffer
+ ShortBuffer

这些缓冲区覆盖了IO中可以利用的数据的基本类型：byte，short，int，long，float，double和characters。
Java NIO也有MappedByteBuffer，可以结合内存映射文件使用。这部分将会留到介绍缓冲区的章节。

####选择器
通过选择器可以实现单个线程处理多个通道事件。如果你的应用存在同时有多个连接打开，而每个连接的通信量不大的情况，那么这将会带来巨大便利。例如，你的应用是聊天程序。
如下是单个线程利用选择器处理处理三个通道的示意图：

![2](http://scalaboy.top/blogPicture/overview-selectors.png)

**&ensp;&ensp;Java NIO：单线程利用选择器处理多通道**

首先要注册通道到选择器，之后通过调用select()开始工作。这个方法将会阻塞线程直到某个已经注册的通道完成工作并触发事件。一旦方法返回，线程就可以着手处理这些事件。