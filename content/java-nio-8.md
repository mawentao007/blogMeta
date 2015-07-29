Title: Java NIO-8 教程
Date: 2015-7-29 
Category: JAVA
Tags:NIO,教程,JAVA

Java NIO(New IO)是Java API中一个可选的IO接口，可以用来作为标准Java IO和Java网络接口之外的一个选择方案。Java NIO提供一个不同和标准IO不同的IO方式。

##Java NIO：通道和缓冲区
在标准的IO API中，通信是以字节流或者字符流来进行的。而在NIO中则需要和通道（channel）以及缓冲区（buffers）打交道。数据通常由通道读入缓冲区，或者由缓冲区写入通道。

##Java NIO：非阻塞IO
Java支持非阻塞模式的IO。例如，一个线程可以请求通道将数据读入缓冲区，而当通道在将数据读入缓冲区的同时，线程可以转头去做其它工作。一旦数据被完全读入缓冲区，线程可以再回来继续处理。将数据写入通道的操作模式也类似。
##Java NIO：Selectors
Java NIO包含“选择器”（selectors）的概念。一个选择器是一个可以监控多个通道事件（连接打开，数据到达等）的对象。通过这种方式，一个线程可以监控多个通道内的数据。
