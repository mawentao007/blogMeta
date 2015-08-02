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
	<img class=embeded-img src="./images/buffers-modes.png">
</p>
<p align="center">
**capacity,position和limit在读写模式下的含义**
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

**clear()和compact()**

一旦完成从缓冲区读取数据，在进行写入之前，必须调用*clear()*或者*compact()*来清理缓冲区。

*clear()*将*position*设置为0，将*limit*设置为*capacity*的值。换句话说，整个缓冲区被清空。但是事实上缓冲区的数据并没有没清理掉，只是改变了相应的标志，将缓冲区存在数据的部分也视为可写。在写入的时候会进行覆盖。

如果缓冲区中有未被读取过的数据，而用户需要在将来某一个时刻继续读取，但是在之前要进行写入操作，那么就要使用*compact()*。

*compact()*将所有未读数据写入缓冲区的开始部分，之后将position设置为紧跟最后一个未读数据的内存单元。*limit*属性依旧是*capacity*值。这时可以继续进行写入，而且未读取的值不会被覆盖。

**mark()和reset()**

用户可以通过调用*Buffer.mark()*标记一个位置，之后可以通过调用*Buffer.reset()*将*position*设置为标记的位置。下面是一个例子：

	buffer.mark();
    //call buffer.get() a couple of times, e.g. during parsing.
    buffer.reset();  //set position back to mark.    

**equals()和compareTo()**
可以通过*equals()*和*compareTo()*来比较两个缓冲区。

满足如下条件则两个缓冲区是*equals*:

+	相同类型
+	有同样数量的剩余数据量
+	所有剩余的数据是相等的

这个方法只比较一部分缓冲区，而不是缓冲区的每个内存元素。事实上它只比较缓冲区剩余的内存元素。

*compareTo()*方法比较两个缓冲区剩余的元素，在某些场景使用，例如排序。满足如下条件则视为一个缓冲区小于另一个：

+	缓冲区中之前的元素和另一个缓冲区对应位置的元素一样，而当前元素比另一个缓冲区的小。
+	两个缓冲区对应位置所有元素一样，但是第一个缓冲区元素较少。

通过上述比较可以发现，这个方法和字符串的比较很相似。





























