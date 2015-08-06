Title: Shell编程
Date: 2015-8-6 
Category: 技术文章
Tags:shell

<i class="fa fa-star-o"></i><h4>文件中按行读取</h4>

	FILE="kv.conf" 
    while read line;
    do
             echo "$line"
    done < $FILE
<i class="fa fa-star-o"></i><h4>判断参数个数</h4>
	
    if [ $# != 1 ]; then
    elif [];then
    else
    fi

<i class="fa fa-star-o"></i><h4>shell函数定义及调用</h4>


shell中的函数的参数列表中没有内容，参数传递在调用过程中进行
	function myFun(){
    	A=$1
  		B=$2
        ...
    }

调用传参如下:

	myFun arg1 arg2

注意在函数调用的时候不要加"()"。

<i class="fa fa-star-o"></i><h4>shell函数进阶</h4>

每个进程都有自己的执行目录，当从shell中执行脚本的时候，脚本实际上是执行在一个新的进程中，因此，“cd”，“pushd”，“popd”等shell内置的命令只能影响当前的进程，相应操作也就无法反映到调用脚本的shell中。

通过定制自己的shell函数，可以增加自定义内置函数，这样就可以将目录的改变映射到所在shell的进程。

要想在当前环境中执行脚本，调用方式如下：

	$ . myscript.sh

使用这种方式，'.'会指定在当前进程中执行脚本，相关的操作就会反映到当前的进程，也就是当前的shell中。而脚本内部定义的函数也将会保留在当前shell的上下文中，可以通过set命令进行查看，也可以通过函数名进行调用。
    
如果要移除上下文中的函数，方法如下：

	$ unset function_name
    
<i class="fa fa-star-o"></i><h4>简单的名称匹配</h4>

	if  [[ $key = $1* ]];then
    	else
    fi
 
 两点注意，一是匹配时候要用双中括号，二是注意'*'的使用。
 

<i class="fa fa-star-o"></i><h4>目录检查</h4>
查看当前名称所指代的是否是一个目录或者文件：

	if [ -d "$DIRECTORY" ]; then
  		# Control will enter here if $DIRECTORY exists.
	fi
    
    if [ -f "$DIRECTORY" ]; then
  		# Control will enter here if $DIRECTORY is file type.
	fi
    
    if [ -L "$DIRECTORY" ]; then
  		# Control will enter here if $DIRECTORY is symbolic link.
	fi
    

<i class="fa fa-star-o"></i><h4>简单ls功能</h4>
	
    for file in folderName
    do 
    	echo $file
    done
    
<i class="fa fa-star-o"></i><h4>参考资料</h4>
<a href = “http://www.gnu.org/software/bash/manual/bashref.html”>
http://www.gnu.org/software/bash/manual/bashref.html
</a>
    

