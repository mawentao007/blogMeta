Title: Git开发模型简介
Date: 2015-9-5
Category: 技术文章
Tags:Git

<a href=http://nvie.com/posts/a-successful-git-branching-model>原文链接</a>

这是一篇介绍git开发模型的文章，原文链接如上，略有删减，保留核心内容。
<p align="center">
	<img class=embeded-img src="./images/git/git-model.png" width="500px">
</p>

<h4>&#9734;&nbsp;为什么选择git</h4>

关于Git和其它代码控制工具的优缺点的比较一直是争论焦点。作为一个开发者，我倾向于使用Git。Git改变了开发者对于merging和branching的看法。我曾经使用经典的CVS/Subversion，merging/branching一直是我比较担忧的部分，并且不能频繁操作。

有了Git，这些操作变得简单可靠，并且可以根据需求随时使用。再也不需要惧怕branching和merging，版本控制工具给branching/merging操作了带来前所未有的便利。

介绍了工具，下面我们来聊一下开发模型。每个开发团队都要通过一系列的操作进行版本控制，本文介绍的模型不外乎也是由这些基本操作构成。


<h4>&#9734;&nbsp;有中心的去中心化</h4>

branching模型正确工作的前提是有一个“真正的“中心代码库。要记住只有一个分支*被认为*是中心代码库（Git是DVCS，因此理论上讲没有中心代码库这个概念）。下文将该分支表述为"origin",这个称呼对Git用户应该不算陌生。

<p align="center">
	<img class=embeded-img src="./images/git/centr-decent.png" width="500px">
</p>

每个开发者都有过push或者pull到origin的经历。除了这种方式，另一种有效的方式就是两个或多个开发人员组成小组，在代码稳定之前通过互相拉取修改代码实现协同工作。如上图，Alice和Bob，Alice和David，Clair和David构成了三个小队。

在实际操作中这种模式非常简单，Alice定义Git remote并指向Bob的代码库即可。

<h4>&#9734;&nbsp;主分支</h4>

<p>
	<img  class=embeded-img src="./images/git/main-branches.png" width="267px" style="float:right">
</p>

本文介绍的模型受到当前存在的模型的很大启发。中心代码库包含两个无限生命周期的分支：

+	master
+	develop

每个Git用户对于*master*分支都不陌生。和*master*分支同时存在的另一个分支称为*develop*。

*origin/master*分是主分支，HEAD表示该分支处于**production-ready**状态。

*origin/develop*分是另一个主分支，HEAD表示该分支的源码处于最新修改的状态，为下一个版本的发行做准备。这个分支也被称为“integration branch”。项目构建的代码就取自这个分支。

当*develop*分支中的代码达到稳定并做好发行准备时，代码将会被merge到*master*，并且获得一个发行版本号。

因此当修改被merge到*master*时，"理论上"++一个新产品就发布了。在这个操作上通常比较谨慎，理论上讲我们可以在每次对master进行commit的时候，通过Git hook脚本实现自动构建并且更新软件版本。

<h4>&#9734;&nbsp;分支</h4>

本文介绍的开发模型利用一系列辅助分支实现小分队并行开发，简化特性追踪难度，为发行版本做准备以及协助开发人员快速解决在线产品问题。不用于主分支，这些分支的生命周期通常较短，并且最终会被删除。分支包含几种类型如下：

+	Feature branches（特性分支）
+	Release branches（发行分支）
+	Hotfix branches（热修复分支）


<p>
	<img  class=embeded-img src="./images/git/fb.png" height="400px" style="float:right">
</p>

每种分支都有特定的功能以及特殊的使用规则。规则通常包括源分支和目标分支约束。

这些分支只是普通的Git分支而已，在操作上没有任何区别。分支的区别在于我们如何“使用”他们。

<h5>Feature branches</h5>

源分支：
&nbsp;&nbsp;&nbsp;*develop*

目标分支：
&nbsp;&nbsp;&nbsp;*develop*

分支名称转换：
除了master，develop，release-\*,或者hotfix-\*

特性分支（有时也被成为主题分支）通常用来进行未来版本中的新特性的开发。当特性被开发的时候，将要在未来哪个版本进行添加也许并未确定。只要相关的特性的开发工作还在进行中，该分支就会存在。但是这个分支最终将会被merge进*develop*（作为新特性进行添加）分支或者被丢弃。

特性分支只存在于开发者的代码库，不会存在于*origin*库。

<h6>创建特性分支</h6>

	$ git checkout -b myfeature develop
    
<h6>合并特性分支到开发分支</h6>

	$ git checkout develop

    $ git merge --no-ff myfeature
	
	$ git branch -d myfeature	
    
	$ git push origin develop
    
--no-ff标签始终创建新的提交对象，即使遇到fast-forward的情况也不例外。这种方式可以避免丢失特性分支历史内容，实现打包所有commits完成新特性添加。比较如下：

<p align="center">
	<img  class=embeded-img  src="./images/git/merge-without-ff.png" width="600px">
</p>

在后一种情况中，通过Git的历史记录无法确定哪些提交对象实现了一个新特性---用户不得不人工阅读log消息。回滚整个特性在这里是一个令人头疼的问题，而用了--no-ff这些就变得非常容易了。

这种方式会创建一些空的提交对象，但是收益远大于支出。

不幸的是我还没有找到将--no-ff参数加入为git merge默认参数的方式，但是这个参数真的非常重要。

<h5>Release branches</h5>

源分支：
&nbsp;&nbsp;&nbsp;*develop*

目标分支：
&nbsp;&nbsp;&nbsp;*develop* 和 *master*

分支名称转换：
&nbsp;&nbsp;&nbsp;release-*

发行分支主要负责新产品发行前的准备工作。该分支可以保证发行前的所有工作能一丝不苟的完成。不仅如此，该分支还可以监控bug修复，准备发行所需元数据（版本号，构建数据等）。发行分支的存在保证了*develop*分支的干净，以便于进行下一阶段的开发。

创建发行分支的时间点是*develop*分支基本符合发行要求的时候。至少所有的目标特性都要被合并到*develop*分支中。其它不需要在该版本发布的新特性可以不加入---这些特性必须等到这个版本发行之后再加入。

事实上要在创建发行分支的时候分配版本号---而不是更早。在此之前，*develop*分支中包含下个版本的改进内容，但是无法确定下个版本最终是0.3还是1.0。

<h6>创建发行分支</h6>

发行分支由*develop*分支创建而来。例如，当前版本为1.1.5，*develop*分支已经准备好下一个发行版本的代码，并且下一个发行版本定为1.2（而不是1.1.5或者2.0）。创建分支和命名的过程如下：

	$ $ git checkout -b release-1.2 develop   //切换到新分支

	$ ./bump-version.sh 1.2   //运行修改文件名的脚本

	$ git commit -a -m "Bumped version number to 1.2"   //提交
    
这个分支会存在一段时间，直到新版本发行完成。在此过程中，bug的修复工作可以在这个分支上进行（而不是在*develop*分支上）。但是添加新特性是严格禁止的，他们必须被合并到*develop*分支上，等待将来版本再发行。
    
<h6>结束发行分支</h6>

当发行分支已经准备就绪，下面的工作就是分为几步。首先将发行分支并入*master*分支（*master*分支的每个提交都是一个新版本，切记）；下一步，到*master*分支的的提交必须表明修改和添加的新特性；最后，对发行版本的修改需要被merge回*develop*分支，使其包含bug fixes。操作如下：

	$ git checkout master //切换到'master'分支

	$ git merge --no-ff release-1.2  //合并分支

	$ git tag -a 1.2

将分支并入*develop*:

	$ git checkout develop

	$ git merge --no-ff release-1.2

这步可能会导致冲突，如果发生冲突，修改并提交。

最后异步要做的就是删除发行分支。

	$ git branch -d release-1.2

<p>
    <img  class=embeded-img src="./images/git/hotfix-branches.png" height="400px" style="float:right">
</p>


<h5>Hotfix branches</h5>

源分支：
&nbsp;&nbsp;&nbsp;*master*

目标分支：
&nbsp;&nbsp;&nbsp;*develop* 和 *master*

分支名称转换：
&nbsp;&nbsp;&nbsp;hotfix-*

热修复分支和发行分支很相似，他们都用于发行新版本。当产品版本出现严重错误需要被立刻修复的时候，就从*master*分支创建一个热修复分支。

热修复分支的意义在于*develop*分支可以继续开发，同时其他开发人员可以专注于修复bug。

######创建热修复分支

热修复分支从*master*分支创建而来。例如：当前产品分支为1.2，但是出现严重bug，而*develop*分支还不稳定，修复过程如下：

	$ git checkout -b hotfix-1.2.1 master //创建新分支"hotfix-1.2.1"
	
    $ ./bump-version.sh 1.2.1  //修改文件版本
    
	$ git commit -a -m "Bumped version number to 1.2.1"

不要忘记修改版本号。当bug修复完成后，提交：

	$ git commit -m "Fixed severe production problem"
    
######完成热修复分支

当热修复分支修复bug完成，需要合并到*master*，但是也需要合并到*develop*。这部分的工作和发行分支很相似。

首先，merge到*master*分支：

	$ git checkout master

	$ git merge --no-ff hotfix-1.2.1

	$ git tag -a 1.2.1

将分支并入*develop*:

	$ git checkout develop

	$ git merge --no-ff release-1.2.1

一种特殊情况是**当一个发行分支这时候已经存在，那么热修复分支需要合并到这个发行分支而不是develop分支**。

最后，删除热修复分支：

	$ git branch -d hotfix-1.2.1
    
<h4>&#9734;&nbsp;总结</h4>

文章的第一幅图在你的开发过程中会起到至关重要的作用。它构建了一个易理解和共享的开发模型，有助于团队成员更好的完成分支和发行工作。该图的[高清版本](http://nvie.com/files/Git-branching-model.pdf)。













