Title: Java NIO-3 Channel
Date: 2015-7-29 
Category: 技术文章
Tags:NIO,教程,JAVA

Java NIO通道和流在很多方面比较相似，但是还是有一些区别：

+ 你可以向一个通道中写入或者读出数据，但是流只能单向操作（读或者写）
+ 通道支持异步读写
+ 通道总是和Buffer同时出现

正如上面提到的，你可以从通道中读取数据到缓冲区中，也可以将缓冲区中的数据写入通道。下图是一个简单描述：

![1](http://scalaboy.top/blogPicture/overview-channels-buffers.png)

**&ensp;&ensp;Java NIO：通道读数据到缓冲区，缓冲区写数据到通道**

**通道的实现**

Java NIO中有几种最重要的通道实现：

+ FileChannel
+ DatagramChannel
+ SocketChannel
+ ServerSocketChannel

*FileChannel* 负责读写文件。

*DatagramChannel* 利用UDP协议读写数据。

*SocketChannel* 利用TCP协议读写数据。

*ServerSocketChannel* 允许你监听TCP连接，正如web服务器所做的那样。对于每个进入的连接会相应创建一个SocketChannel。

**简单的例子**
```	
    RandomAccessFile aFile = new RandomAccessFile("data/nio-data.txt", "rw");
    FileChannel inChannel = aFile.getChannel();

    ByteBuffer buf = ByteBuffer.allocate(48);

    int bytesRead = inChannel.read(buf);
    while (bytesRead != -1) {

      System.out.println("Read " + bytesRead);
      buf.flip();

      while(buf.hasRemaining()){
          System.out.print((char) buf.get());
      }

      buf.clear();
      bytesRead = inChannel.read(buf);
    }
    aFile.close();
```
注意其中的buf.flip()调用。首先将数据读入Buffer，之后flip，然后将数据读出。



