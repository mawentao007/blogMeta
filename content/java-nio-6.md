Title: Java NIO-6 通道之间数据传输
Date: 2015-8-9 
Category: 技术文章
Tags:NIO,教程,JAVA

Java NIO可以实现通道之间直接通信，前提是其中一个通道是FileChannel。FileChannel有两个方法可以利用：transferTo()和transferFrom()。


<h4>&#9734;&nbsp;transferFrom()</h4>

FileChannel.transferFrom()方法将数据从源通道传输到FileChannel。如下：
```
RandomAccessFile fromFile = new RandomAccessFile("fromFile.txt", "rw");
FileChannel      fromChannel = fromFile.getChannel();

RandomAccessFile toFile = new RandomAccessFile("toFile.txt", "rw");
FileChannel      toChannel = toFile.getChannel();

long position = 0;
long count    = fromChannel.size();

toChannel.transferFrom(fromChannel, position, count);
```
参数position和count记录目标文件中开始写数据的位置，以及传输的最大数据量。如果源通道的数据量小于count，那么传输量也会小于count。

特别指出的是，某些SocketChannel的实现只传输当前已经准备就绪的数据---即使SocketChannel在随后有更多的数据可用，也不会继续传输。因此，从SocketChannel到FileChannel中传输的数据量可能不是整个请求(count)的量。
    

<h4>&#9734;&nbsp;transferTo()</h4>

FileChannel.transferTo()方法将当前FileChannel中的数据传输到目标通道。
```
RandomAccessFile fromFile = new RandomAccessFile("fromFile.txt", "rw");
FileChannel      fromChannel = fromFile.getChannel();

RandomAccessFile toFile = new RandomAccessFile("toFile.txt", "rw");
FileChannel      toChannel = toFile.getChannel();

long position = 0;
long count    = fromChannel.size();

fromChannel.transferTo(position, count, toChannel);
```

这两个例子很相似，参数的意义也一致。

SocketChannel的问题也存在，SocketChannel的实现可能只发送若干FileChannel中传来的数据直到发送缓冲区被填满，然后停止。
