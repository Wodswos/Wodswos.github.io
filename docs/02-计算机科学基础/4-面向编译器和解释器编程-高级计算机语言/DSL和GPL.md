DSL，Domain Special Language

* 以极其高效的方式描述特定领域的对象、规则和运行方式的语言。
* 能够描述特定领域的世界观和方法论的语言。
* 需要有特定的解释器与其配合。



> A computer programming language of limited expressiveness focused on a particular domain.

而有限的表达能力就成为了 GPL 和 DSL 之间的一条界限（DSL并不是图灵完备的）。[^1]



最常见的DSL包括Regex、SQL以及HTML&CSS。

> 以前数模用过的Lingo也算是DSL咯？



# 构建DSL

实现编程语言的过程可以简化为定义语法与语义，然后实现编译器或者解释器.

而 DSL 的实现与它也非常类似，我们也需要对 DSL 进行语法与语义上的设计。

* 设计语法和语义，定义DSL中的元素是什么样的以及代表什么意思
* 实现parser，对DSL解析，并通过解释器执行







[^1]:https://www.cnblogs.com/feng9exe/p/10901595.html