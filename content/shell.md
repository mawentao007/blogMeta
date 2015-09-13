Title: Shell编程
Date: 2015-8-9 
Category: 技术文章
Tags:shell

<h4>&#9734;&nbsp;文件中按行读取</h4>
	
    FILE="kv.conf" 
    while read line;
    do
             echo "$line"
    done < $FILE
<hr>

<h4>&#9734;&nbsp;判断参数个数</h4>
	
    if [ $# != 1 ]; then
    elif [];then
    else
    fi
<hr>

<h4>&#9734;&nbsp;shell函数定义及调用</h4>

shell中的函数的参数列表中没有内容，参数传递在调用过程中进行

	function myFun(){
    	A=$1
  		B=$2
        ...
    }

调用传参如下:

	myFun arg1 arg2

注意在函数调用的时候不要加"()"。
<hr>

<h4>&#9734;&nbsp;shell函数进阶</h4>

每个进程都有自己的执行目录，当从shell中执行脚本的时候，脚本实际上是执行在一个新的进程中，因此，“cd”，“pushd”，“popd”等shell内置的命令只能影响当前的进程，相应操作也就无法反映到调用脚本的shell中。

通过定制自己的shell函数，可以增加自定义内置函数，这样就可以将目录的改变映射到所在shell的进程。

要想在当前环境中执行脚本，调用方式如下：

	$ . myscript.sh

使用这种方式，'.'会指定在当前进程中执行脚本，相关的操作就会反映到当前的进程，也就是当前的shell中。而脚本内部定义的函数也将会保留在当前shell的上下文中，可以通过set命令进行查看，也可以通过函数名进行调用。
    
如果要移除上下文中的函数，方法如下：

	$ unset function_name
<hr>
   
<h4>&#9734;&nbsp;简单的名称匹配</h4>

	if  [[ $key = $1* ]];then
    	else
    fi
 
 两点注意，一是匹配时候要用双中括号，二是注意“*” 的使用。
<hr>
 
<h4>&#9734;&nbsp;目录检查</h4>

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
<hr>
    
<h4>&#9734;&nbsp;简单ls功能</h4>
	
    for file in folderName
    do 
    	echo $file
    done
<hr>
    
<h4>&#9734;&nbsp;管道</h4>

	command1  [ | or |& ] command2

其中*'|&'*表示将第一个命令的标准输出连同错误都作为第二个命令的标准输入。
<hr>

<h4>&#9734;&nbsp;&结尾</h4>

'&' 结尾的命令，shell将会在子shell中异步执行相应的命令，也就是通常说的“后台执行”。

<hr>
<h4>&#9734;&nbsp;循环</h4>

**until**

	until test-commands;
    do   
          commands;
    done


**while**
	
    while test-commands; 
    do 
    	consequent-commands; 
    done

**for**

	for name [ [in [words …] ] ; ] 
    do 
    	commands; 
    done
    
    for (( expr1 ; expr2 ; expr3 )) ;
   	do 
    	commands ; 
    done

*break* and *continue*用法类似c语言的用法，可以在循环中起到控制作用。
<hr>

<h4>&#9734;&nbsp;分支结构</h4>

**if**
```
if test-commands; then
  consequent-commands;
[elif more-test-commands; then
  more-consequents;]
[else alternate-consequents;]
fi
```

**case** 这个结构略微复杂一点，格式和示例如下：

	case word in [ [(] pattern [| pattern]…) command-list ;;]… esac

    echo -n "Enter the name of an animal: "
	read ANIMAL
	echo -n "The $ANIMAL has "
	case $ANIMAL in
  	horse | dog | cat) echo -n "four";;
  	man | kangaroo ) echo -n "two";;
  	*) echo -n "an unknown number of";;
	esac
	echo " legs."
    
其中必须注意的是，每个分支结尾用‘;;’，表示一旦某一个分支匹配成功就不再继续匹配；‘;&’表示对紧随当前分支的下一个分支的命令也同时执行；‘;;&’表示需要检查下一个分支是否匹配，匹配的话执行相应命令。

**select**

	select name [in words …]; do commands; done
    
    eg.
    select fname in *;
	do
		echo  $fname \($REPLY\)
	break;
	done
    
根据用户输入选项，从若干个选项中选择一个，将值赋给name。例子中$REPLY表示用户的输入。备选项可以由命令行输入，用$@读取。例子表示从当前目录的文件中选择一个，打印出所选的文件名和所选项。
	
**（（...））**

	(( expression ))  等同于
    let "expression"
    
    eg.
    if (( 1 + 2 )) ;    //if let "1 + 2";
	then                                                                            
        echo "true"
	fi
计算括号中表达式的值，根据值是否为０返回０或者１，参见例题。要注意括号内侧的两个空格。

**[[...]]**
	
    [[ expression ]]
    
根据表达式的真假值返回０或者１。这个用法比较复杂，可以用来进行模式匹配的相关判断，参见http://www.gnu.org/software/bash/manual/bashref.html#Looping-Constructs。
<hr>

<h4>&#9734;&nbsp;数组</h4>

```
declare -a arr   #声明数组，可以省略。
for (( i=0;i<10;i++ )); 
do
        arr[$i]=$i
done
for (( i=0;i<10;i++ )); 
do
        echo ${arr[$i]}
done
```
<hr>

<h4>&#9734;&nbsp;简单读取</h4>

&#9723;&nbsp;**ReadArray**
从文件中读取数据存入数组中。

	readarray x < $FILE                                             
    echo ${x[0]}

&#9723;&nbsp;**Read**
可以从文件或者标准输入读取数据，注意一次读取的默认也是一整行，其它模式参见相关文档。

	read x                                              
    echo $x
<hr>

<h4>&#9734;&nbsp;按列截取文档</h4>

截取相应列并返回截取的内容
	
    cut -d " " -f 3- input_filename > output_filename
    -d  后面跟分隔符，默认tab
    -f  选择内容段，按列索引，起始值为1，3-表示截取第三列及其之后的列，没有“-”则表示删除对应列。

<h4>&#9734;&nbsp;参考资料</h4>
<a href = “http://www.gnu.org/software/bash/manual/bashref.html”>
http://www.gnu.org/software/bash/manual/bashref.html
</a>
    

