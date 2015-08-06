Title: Na目录切换工具"哪"
Date: 2015-8-6
Category: 个人项目
Tags:目录,小工具

<h5>[地址](https://github.com/mawentao007/na)</h5>
<p align="center">
<img class="embeded-img" src="/images/na.jpg">
</p>
***
<i class="fa fa-star-o"></i><h4>功能描述</h4>
cd命令的扩展工具，支持对目录添加别名进行切换。
        
        $ na 
        $ na dir               切换到目录 
        $ na ~                 切换到$HOME目录
        $ na 别名              切换到别名指代的目录

***
<i class="fa fa-star-o"></i><h4>配置</h4>

将脚本放置在$HOME目录下，在.bashrc中添加如下语句:

	. na.sh  
   
特别注意第一个‘.’
    
别名的配置文件为
	
    $HOME/.kv.conf
    
***
<i class="fa fa-star-o"></i><h4>使用方法</h4>

          usage: na [-h|-a|-d] folderName
                     -h      help
                     -a      add alias
                     -d      remove alias
                     -l      list all alias
