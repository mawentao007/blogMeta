Title: Java NIO-4 Buffer
Date: 2015-8-1 
Category: 技术文章
Tags:NIO,教程,JAVA

Java NIO缓冲区是和NIO通道进行交互，共同工作的。

一个缓冲区实际上是是一块内存区域，可以用来读写数据。这块内存区域被一个NIO缓冲区对象封装起来，这个对象提供了一系列方法来方便对该内存块进行操作

**基本的缓冲区用法**

使用一个缓冲区进行读写通常需要四个步骤：

1.	将数据写入缓冲区
2.	调用*buffer.flip()*
3.	从缓冲区读出数据
4.	调用*buffer.clear()*或者*buffer.compact()*

当用户向缓冲区写入数据的时候，缓冲区会记录写入数据量。一旦需要读取数据，则需要调用*flip()*函数将缓冲区由写模式切换到读模式。

一旦所有的数据都被读出，用户需要清除缓冲区来为下一次写入做准备。清除缓冲区可以通过*clear()*或者*compact()*两个方法实现。*clear()*方法清除整个缓冲区，而*compact()*方法只清除刚刚读取过的数据。任何未读取数据都将被移动到缓冲区起始位置，新写入的数据将会被追加到未读取数据之后。

下面是一段使用缓冲区的示例代码：

```
RandomAccessFile aFile = new RandomAccessFile("data/nio-data.txt", "rw");
FileChannel inChannel = aFile.getChannel();

//create buffer with capacity of 48 bytes
ByteBuffer buf = ByteBuffer.allocate(48);

int bytesRead = inChannel.read(buf); //read into buffer.
while (bytesRead != -1) {

  buf.flip();  //make buffer ready for read

  while(buf.hasRemaining()){
      System.out.print((char) buf.get()); // read 1 byte at a time
  }

  buf.clear(); //make buffer ready for writing
  bytesRead = inChannel.read(buf);
}
aFile.close();
```

**缓冲区容积(Capacity)，位置(Position)和界限(Limit)**

一个缓冲区对象有三个用户必须熟悉的熟悉，只有熟悉这些属性才能更好的理解缓冲区的工作原理：

+	capacity
+	position
+	limit

其中*position*和*limit*的含义取决于当前缓冲区处于何种模式。*Capacity*的含义是在不同模式下是一致的。

下面有一个例子来讲解这三个属性在不同模式下的意义：
<p align="center">
	<img class=embeded-img src="{{SITEURL}}/images/buffer-modes.png">
</p>
<p align="center">
==capacity,position和limit在读写模式下的含义==
</p>

**Capacity**

这个属性表示相应的缓冲区的大小，用户能操作的当前缓冲区的空间不超过这个属性值。一旦缓冲区被填满，则必须先清空缓冲区（读出数据或者调用*clear*）才能继续写入。

**Position**

用户向缓冲区写入数据需要从*position*开始，初始状态这个值是0。当有数据写入缓冲区，*position*移动到下一个可写入的内存单元。*Position*最大只能到*capacity - 1*。

当用户从缓冲区读取数据时，也要从*position*开始。当用户将缓冲区由写模式切换到读取模式，*position*被设置为0。随着读取的进行，*position*向下一个可读取的位置移动。

**Limit**

在写模式下这个熟悉就代表整个缓冲区的大小，和*capacity*的值相等。

当缓冲区切换到读取模式，*limit*表示总共可读出的数据的大小。因此，当调用*flip()*由写模式切换到读取模式的时候，*limit*被设置为写模式*position*所在的位置。换句话说，用户可以读取的数据就是被写入的数据的大小。

**缓冲区类型**

+	ByteBuffer
+	MappedByteBuffer
+	CharBuffer
+	DoubleBuffer
+	FloatBuffer
+	IntBuffer
+	LongBuffer
+	ShortBuffer

*MappedByteBuffer*比较特殊，请参照相关文档。

**分配缓冲区**

每个缓冲区类型都有一个*allocate()*方法用来分配空间。如下：

	ByteBuffer buf = ByteBuffer.allocate(48);
 
下面是一个例子，分配一个大小为1024个字符的*CharBuffer*

	CharBuffer buf = CharBuffer.allocate(1024);

**写入缓冲区**

有两种方法可以向缓冲区写入数据:

+	从通道中将数据写入缓冲区
+	利用*put()*方法直接向缓冲区写入数据

如下展示的是由通道向缓冲区写数据:
	
    int bytesRead = inChannel.read(buf); //read into buffer.

如下是用*put()*方法写缓冲区：

	buf.put(127); 

> *put()*有很多版本，每个版本功能不尽相同，请参照JavaDoc选择使用。

**rewind()**

*Buffer.rewind()*方法设置*position*为0，不改变*limit*的值。
****
http://tutorials.jenkov.com/java-nio/buffers.html



























