Title:Scala Array Pattern Matching问题
Date: 2015-7-31 
Category: 技术文章
Tags:Scala,Array,Pattern Matching

问题如下：给出两个整数队列，合并并排序。

这个问题并不难，Scala提供的工具函数可以很简单的解决。首先定义变量：

	val a = Array(1,3,5)
    val b = Array(2,4,6)
这里声明两个数组a和b，如下是解决办法。
####第一种方法

	(a ++ b).sorted
这个方法通俗易懂，不多加解释了。

####第二种方法

	def mergeSort(a: Array[Int], b: Array[Int],ans:ArrayBuffer[Int]): Array[Int] = {
 	(a, b) match {
 		case (Array(m, _*), Array(n, _*)) => if (m < n) {
 			ans += m
 			mergeSort(a.tail, b,ans)
          } else {
            ans += n
            mergeSort(a, b.tail,ans)
          }
        case (_, Array()) => ans ++= a
      	case (Array(),_) => ans ++= b
          }
 		ans.toArray
	}

利用数组进行模式匹配，递归，逐个选出当前最小的元素加入结果队列。

####第三种方法

```
def listMergeSort(a: List[Int], b: List[Int],ans:ListBuffer[Int]): Array[Int] = {
  (a, b) match {
    case (m::x, n::y) => if (m < n) {
      ans += m
      listMergeSort(x,b,ans)
    } else {
      ans += n
      listMergeSort(a, y,ans)
    }
    case (Nil,_)=> ans ++= b
    case (_, Nil) => ans ++= a
  }
  ans.toArray
}

```
这种方法略显笨重，将队列先转换为List，利用List来进行模式匹配获得结果，用最熟悉的方式解决问题。