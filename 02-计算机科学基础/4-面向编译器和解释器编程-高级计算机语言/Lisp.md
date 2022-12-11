[^]: 

# 概述

* 历史
* 方言

Common Lisp和Scheme合称为两大Lisp方言。



## 参考资料

《Structure and Interpretation of Computer Programs》（电子材料官网：https://mitpress.mit.edu/sites/default/files/sicp/index.html）及其配套MIT网课

《Practical Common Lisp》《Land of Lisp》《The little Schmer》（Daniel P. Friedman, Matthias Felleisen著，卢俊祥译,中译版副标题为递归与函数式的奥妙）适合初学

《On Lisp》和《Let over Lambda》主要讨论宏

《计算机程序的结构和解释》公开课 翻译项目 https://github.com/DeathKing/Learning-SICP

还有《Lisp in small pieces》《Essentials of Programming Language》等



### 文章 & 博客

怎样写一个解释器 http://www.yinwang.org/blog-cn/2012/08/01/interpreter

《Lisp已死，Lisp万岁》王垠http://www.yinwang.org/blog-cn/2013/03/26/lisp-dead-alive 

《Chez Scheme 的传说》王垠 http://www.yinwang.org/blog-cn/2013/03/28/chez-scheme

《Teach Yourself Programming in Ten Years》http://norvig.com/21-days.html 

# Common Lisp

1984年，改良自MacLisp、集各版本大成、跨平台、且被目为事实标准的Common Lisp诞生。至1994年，美国国家标准学会(ANSI)对Common Lisp语言进行了标准化。

自稳定运行的Common Lisp出现起，再有各机构按各自所需而开展后续Lisp，包括1990年来自欧洲用户的EuLisp及自由开源的IsLisp，ACL2等。

## CLISP

GNU CLISP. An ANSI Common Lisp Implementation.



# Scheme

http://wingolog.org/archives/2013/01/07/an-opinionated-guide-to-scheme-implementations

## Racket

 http://racket-lang.org/

* 可以简单理解为 scheme 超集
* Racket 允许使用方括号而不只是圆括号，两者可以互换（但要配对，不能左圆右方那种）



## Chez Scheme

> Chez Scheme Windows下安装的时候好像不太支持自定义安装路径的样子。

# 其他方言

## Emacs Lisp

一种直译式的脚本语言，为LISP的方言之一，GNU Emacs与XEmacs文字编辑器都使用这个编程语言来扩展他们的功能。

## Clojure





# 青梅竹马：LISP和AI

https://blog.youxu.info/2009/08/31/lisp-and-ai-1/

https://blog.youxu.info/2009/08/31/lisp-and-ai-2/

## 人工智能的初期发展

二战后的蓬勃的人工智能初步发展：

* 1948年维纳发表了《控制论》，副标题《动物和机器的控制通信》
  * 看中文版译者的序，了解到苏联当时是抵触维纳和控制论的，认为将人物化了，机械主义了
* 1949年，香农提出了可以下棋的机器
* 1949年，加拿大Donald Hebb发表“行为的组织”，开创了神经网络的研究。
* 1950 年，图灵发表了著名的题为“计算的机器和智能”的文章，提出了著名的图灵测试

不得不说，这样的盛景，可比现在算力堆叠的深度学习还要来得蓬勃。

## Why LISP?

LISP=LISt Processing。

 AI 的输入数据通常非常多样化，而且没有固定格式。 比如一道要求解的数学题，一段要翻译成中文的英文，一个待解的 sodoku 谜题，或者一个待识别的人脸图片。 所有的这些， 都需要先通过一个叫做“知识表示”的学科，表达成计算机能够处理的数据格式。

自然，计算机科学家想用一种统一的数据格式表示需要处理多种多样的现实对象， 这样， 就自然的要求设计一个强大的，灵活的数据格式。 这个数据格式，就是链表。

> 作者此处推荐阅读SICP……那我岂不是真的要在CS的路上一去不复返了？我明明该学SE转AI的啊啊啊啊

AI 研究关心于符号和逻辑计算远大于数值计算，比如下棋，就很难抽象成一个基于纯数字的计算问题。

而数组等数据结构，并不能很好地存储不同结构的数据。

* 链表的充分性：列表是否能够充分的表示所有的人工智能问题
* 人工智能是否的确能够通过对列表的某种处理方法获得

> A physical symbol system has the necessary and sufficient means for general intelligence action.

让当时几乎所有的研究者，把宝押在了实现一个通用的符号演算系统上，因为假如我们制造出一个通用的基于符号演算的系统，我们就能用这个系统实现智能。

可惜，事实似乎并不是这样。

> 链表和函数式编程是两个互相正交的概念，即既可以有链表函数式编程，也可以有非链表函数式、链表面向过程，以及通常的非链表面向过程。

## AI范式的演变

最早期冯诺依曼这一学派的哲学很清晰： 人类大脑是一个标准的智能体，我们只需要让计算机模拟人的大脑的工作方式，计算机就有了和人类大脑一样的智能了。 

他们相信大脑的结构和工作机理决定了智能，至于大脑是用脑细胞构成的，还是用电子电路模拟的，对于智能来说毫不重要。

从脑科学和认知科学的角度去分析智能在当时有一个非常大的局限: 脑神经解剖学本身不成熟。 上个世纪 80 年代前成功实施的一些人工智能系统，极少是来自于连接主义学派的。直到80年代后随着 BP 算法的重新发现，联接主义才迎来了第二春。 

在LISP被称为AI语言的那个年代，联结主义几乎没啥话语权，不像现在张口闭口深度学习，神经网络。

当我们把 LISP 放到这段历史中，就会自然的想到， 什么语言适合人工智能的问题，就变成了“什么语言能做符号处理”。

当然LISP是最能做符号处理的。

## S-Expression

LISP中统一表示程序和数据的方法。S是Symblic的意思。用现代编程语言的话说，LISP支持meta-programming。

LISP 程序可以处理，生成和修改 LISP 程序。这个特性，加上函数是一阶对象的特性，使得 LISP 远远比同时代的任何语言灵活。LISP 的这种灵活，恰好满足了基于符号处理的 AI 领域对语言的“强大的表达能力”（可以对任何复杂系统建模）和“高层的抽象能力” 的需求。

这二十年来，AI 研究领域接连发生了好几个非常大的 paradigm shift. 传统的基于符号的 AI 方法不再是主流，取而代之的，是多种多样的基于统计的，基于自动推理的，基于机器学习的，基于群体智慧的，基于大规模数据集的等等各种各样研究方法的兴起。

> 可能作者写这篇文章的时候还很早，甚至deep learning都还不流行，所以没有提到吧。

大多写编程语言书的作者，未必全部知晓这个变化，因此还沿袭原来的框架，继续写下 “LISP是适合 AI 的编程语言” 这样一个早就不能完全反映现状的断言。



> 以上都是对原博文的摘抄和片段截取。
>
> 但个人倒觉得现在deep learning越来越泛滥，反而有必要重新拾起LISP，或者说拾起符号主义，谁知道下一个浪潮是哪个主义掀起呢。
