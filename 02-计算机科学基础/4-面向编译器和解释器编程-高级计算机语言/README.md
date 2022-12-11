

![](C:/Users/Five/Desktop/note/img/which-programming-language-should-i-learn-first-infographic.png)

# 语言的变迁[^2]

编年史：

* 1957年，John Backus创建了第一套高阶语言FORTRAN
* 1959年，霍普发明第一个面向企业、面向业务的编程语言COBOL（Common Business-Oriented Language）
* 1964年，John Kemeny和Thomas Kurtz认为需要回到基础，发明编程语言BASIC
* 1970年，Niklaus Wirth设计并创立了Pascal
  * 维尔特后来开发了类似Pascal的Modula-2和Oberon
  * 提出了著名的“算法+数据结构=程序”
  * GCC最初由Pascal的一种方言Pastel编写。
* 1972年，丹尼斯·里奇在贝尔实验室开发出C语言。
  * C语言是以B语言为基础开发的。
  * 1973年，Dennis Ritchie用C语言改写原来用汇编语言编写的UNIX，由此产生了UNIX Version V
* 1980年，Alan Kay设计了Smalltalk
  * Smalltalk中一切都是对象，某种程度上的面向对象开山之作
* 1987年，Larry Wall发布Perl 1.0
  * 最初被当做一种跨平台环境中书写可移植工具的高级语言
  * 最初是为文本处理而开发的，现在用于各种任务，包括系统管理，Web开发，网络编程，GUI开发等。
  * 内部集成了正则表达式的功能，以及巨大的第三方代码库CPAN
* 1991年，Guido van Rossum不喜欢花括号，于是他发明了Python
  * 语法选择的灵感来源自Monty Python和Flying Circus
* 1995年，James Gosling发明了Java
* 同年，Brendan Eich花了个周末设计了门语言，称之LiveScript
  * Java在代码审查环节火了，于是他们决定用大括号才好，改名叫JavaScript。
  * 后来Java一团糟，于是他们觉得这语言跟Java沾亲带故会出事，所以又在标准化时候把它改名叫ECMAScript
* 2001年，Anders Hejlsberg重建了Java，并称之为C#
* 2009年，Go问世
* 2010年，Rust问世

## C/C++ YYDS



## Java的兴起

`Write Once, Run Anywhere`



### 解释or编译？

C#到底属于编译型语言还是解释型语言？ - 皮皮关的回答 - 知乎 https://www.zhihu.com/question/420335415/answer/1556912500

但是在实践中有两个趋势，“解释型语言”越来越“编译”，“编译型语言”越来越“解释”。

即使是编译型语言如C++，又何尝不是依托于操作系统；随着语言提供的功能越来多，Runtime 愈加厚重，权力也越来越大。

即使是解释型语言如Python，也提供许多手段让他显得更“编译”，如 PyPy 应用了 JIT 技术。



当然也还是可以区分的，解释器和编译器差异还是很大。

https://www.iteye.com/blog/rednaxelafx-492667

### JIT——解释和编译的破壁人



## 解释语言大繁荣

`Write Once, Run Anywhere`是当年Java的Slogan，也是Java脱颖而出的重要原因，以今天的角度来看，这件事对Python等解释语言而言也是小菜一碟。

> 害，年少轻狂，曾经瞧不起解释语言，现在只能说真香。（不过依旧体会不到JS的精髓）
>
> 如果是以实验、验证为主要目的，谁在乎那一点点执行速度呢。

### VM vs Interpreter[^3][^4]

关于虚拟机（Virtual Machine）维基百科有如下两种定义：

* System virtual machine
  * provide a substitute for a real machine
* Process virtual machine
  * designed to execute computer programs in a platform-independent environment.

显然，JVM是后者

> A virtual machine is a virtual computing environment with a specific set of atomic well defined instructions that are supported independent of any specific language and it is generally thought of as a sandbox unto itself. The VM is analogous to an instruction set of a specific CPU and tends to work at a more fundamental level with very basic building blocks of such instructions (or byte codes) that are independent of the next. An instruction executes deterministically based only on the current state of the virtual machine and does not depend on information elsewhere in the instruction stream at that point in time.[^4]



### 字节码 vs 文本源码

> 通常，解释器指的是读取文本源码，生成AST执行之；而虚拟机指的是文本源码先被编译成VM能理解的bytecode（类似汇编），VM执行之。
>
> 常说「Java 在虚拟机中运行」，请问这个虚拟机可以视为 Java 语言的解释器吗？ - 知乎 https://www.zhihu.com/question/20667732/answer/81166406





### 补充

个人的初步理解大致如下图所示

![](C:/Users/Five/Desktop/note/img/compile_vs_interpret.png)

# C/C++编译器简史

## 第一个C语言编译器

第一个C语言编译器是由汇编语言写的。

> The first C compiler written by Dennis Ritchie used a recursive descent parser, incorporated specific knowledge about the PDP-11, and relied on an optional machine-specific optimizer to improve the assembly language code it generated.
>
> from wiki



## C++编译器

第一个C++编译器（Cfront）是用C with Classes写的（一种C的方言）。

> The first C++ compiler (Cfront) was written in C++. 
>
> To build that, I first used C to write a "C with Classes"-to-C preprocessor. "C with Classes" was a C dialect that became the immediate ancestor to C++. 
>
> That preprocessor translated "C with Classes" constructs (such as classes and constructors) into C. It was a traditional preprocessor that didn't understand all of the language, left most of the type checking for the C compiler to do, and translated individual constructs without complete knowledge. I then wrote the first version of Cfront in "C with Classes".





# 学习资源和参考资料[^1]









[^1]:https://carlcheo.com/startcoding
[^2]:http://dwz.win/kpF
[^3]:凭啥Java的运行环境称虚拟机，Python的只能称解释器 - 安静的程序员的文章 - 知乎 https://zhuanlan.zhihu.com/p/58167547
[^4]:https://stackoverflow.com/questions/441824/java-virtual-machine-vs-python-interpreter-parlance/441973#441973
[^5]:https://www.iteye.com/blog/rednaxelafx-492667
