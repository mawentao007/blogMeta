Title: Java NIO-8 文件通道
Date: 2015-9-15 
Category: 技术文章
Tags:NIO,教程,JAVA
Summary:Java NIO 文件通道是用来连接文件的通道。通过文件通道可以对文件进行读写操作。Java NIO文件通道是Java IO API之外的读写文件的另一个选择。

<a href=http://tutorials.jenkov.com/java-nio/file-channel.html>原文链接</a>

Java NIO 文件通道是用来连接文件的通道。通过文件通道可以对文件进行读写操作。Java NIO文件通道是Java IO API之外的读写文件的另一个选择。


<h4>&#9734;&nbsp;打开文件通道</h4>

使用文件通道之前必须要先打开一个通道。文件通道无法直接打开，必须通过InputStream、OutputStream或者RandomAccessFile来打开。利用RandomAccessFile打开文件通道的代码如下：

	RandomAccessFile aFile     = new RandomAccessFile("data/nio-data.txt", "rw");
	FileChannel      inChannel = aFile.getChannel();
    
<h4>&#9734;&nbsp;从文件通道读取数据</h4>

从文件通道读取数据需要调用一种*read()*方法：

	ByteBuffer buf = ByteBuffer.allocate(48);

	int bytesRead = inChannel.read(buf);
    
首先分配一个缓冲区，从文件通道中将数据读入该缓冲区。之后调用*FileChannel.read()*方法进行读取。该方法从文件通道中将数据读入缓冲区。返回值表示写入缓冲区的字节数。如果返回-1，说明到达了文件结尾。

<h4>&#9734;&nbsp;将数据写入文件通道</h4>

将数据写入文件通道要利用到*FileChannel.write()*方法，该方法需要一个Buffer作为参数，如下：

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

注意while循环中*FileChannel.write()*的调用方式。因为*write()*方法写入文件通道的字节数无法确定，因此需要重复调用*write()*方法知道Buffer中没有可以进行写入的数据。

<h4>&#9734;&nbsp;关闭文件通道</h4>

	channel.close();
    
<h4>&#9734;&nbsp;文件通道中的位置</h4>

对于文件通道的读写都会在特定位置进行，用户可以通过*position()*方法获得通道对象当前的位置，也可以通过*position(long pos)*方法指定通道中的位置。如下：
	long pos channel.position();

	channel.position(pos +123);

如果用户将位置设置为文件结尾，并尝试从通道中读取数据，那么将会返回-1。

如果用户将位置设置为文件结尾并尝试写入通道，文件将会扩展并写入数据。这可能会导致“file hole”，磁盘上的文件存在空洞。

<h4>&#9734;&nbsp;文件通道的尺寸</h4>

*size()*方法可以返回文件通道连接的文件的大小。

	long fileSize = channel.size(); 

<h4>&#9734;&nbsp;文件通道截取</h4>

*FileChannel.truncate()*方法可以截取文件的特定长度。
	
    channel.truncate(1024);

该示例截取了文件的1024字节内容。

<h4>&#9734;&nbsp;文件通道强制执行</h4>

*FileChannel.force()*方法将所有未写入数据从通道中“刷”到磁盘上。操作系统为了提升性能会在内存中缓存一部分数据，因此用户无法保证写入通道中的数据真正写入到磁盘上。而调用*force()*方法之后就不存在这个问题了。

*force()*方法有一个布尔值作为参数，标明元数据是否也需要flush。eg.

	channel.force(true);














