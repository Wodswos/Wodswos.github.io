# Java常识

## 类的加载和对象的实例化[^2]

1. 类在首次被使用（访问静态成员或者创建类的实例）会触发类的加载
2. 类的加载会触发静态成员的初始化、静态代码块的执行。
3. 完成类的加载和静态成员的初始化后会初始化一个实例并返回





![](C:/Users/Five/Desktop/note/img/19471645-37eadc0b514509bd.png)

![](C:/Users/Five/Desktop/note/img/19471645-87b0398fb493959d.jpg)



### 类的加载[^2]

* 加载
  * 根据类的全限定名获取类的二进制字节流。
  * 将二进制字节流所代表的静态存储结构转化为方法区中运行时数据结构。
  * 在内存中创建一个代表该类的Java.lang.Class对象，作为方法区这个类的各种数据的访问入口。
* 验证
* 准备
* 解析
* 初始化
* 使用
* 卸载



###  静态代码块







> 还有直接`{}`（没有注明static）的代码块，优先级还是比构造函数高。

## volatile和指令重排序

https://www.bilibili.com/video/BV1Q5411T7FY

最经典的就是在单例模式中给instance增加volatile关键字，防止字节码层面（或更底层）的指令重排序可能会导致的问题。



## psvm

`public static void main(String[] args)`，Java程序的入口

main方法必须严格遵循它的语法规则，方法签名必须是public static void，参数是字符串数组类型。



在《Java语言规范》中，对于Java虚拟机的启动给出了明确的定义：Java虚拟机是通过加载指定的类，然后调用该类中的main方法而启动的。[^1]

更多细节可以参考下图[^3]：

![](C:/Users/Five/Desktop/note/img/v2-ca1a8f0cb36bb25f7a147e2d52ab0051_b.jpg)





> 为什么 Java 的 main 是 void，而 C++ 标准却推荐 `int main()`。



# 序列化

其实一直很疑惑这个东西，因为在内存中是01的二进制数据，在磁盘上也是01的二进制数据，在网络上传输还是01的二进制数据——为啥要整这序列化和反序列化的东西呢？



> java的序列化能让你将一个实现了 Serializable 接口的对象转换成一组 byte

可是，如果不序列化，难道他在内存中就不是Byte了吗？难不成内存中除了01还能有2？



# JVM

> Java的`.class`文件的魔数还有小彩蛋，用十六进制表示是`cafe babe`，和其Logo呼应。





## Hotspot和JIT[^4][^5][^6]

Just-In-Time compilation，或称Dynamic translation、run-time compilations.

JIT compilation is a combination of the two traditional approaches to translation to machine code ([ahead-of-time compilation](https://en.wikipedia.org/wiki/Ahead-of-time_compilation) (AOT), and [interpretation](https://en.wikipedia.org/wiki/Interpreter_(computing))) and combines some advantages and drawbacks of both.



在Hotspot Code主要有两类

* 被多次调用的方法
* 被多次执行的循环体

### 解释器和编译器的互补共生

* 解释器可以作为编译器“激进优化”操作的退路，当“激进优化”的条件不成立时，退而求其次，转为解释器执行



### Client Compiler和Server Compiler

编译器的分层策略

* 第0层，程序解释执行，解释器不开启性能监视功能（Profiling），可触发第1层编译。
* 第1层，也称为C1（Client Compiler）编译，将字节码编译成本地代码，进行简单、可靠的优化，若有必要将加入性能监控的逻辑
* 第2层，也称为C2（Server Compiler）编译，也是将字节码编译成为本地代码，但是会启动一些编译耗时较长的优化，甚至会根据性能监控进行一些不可靠的激进优化。

### Graal

GraalVM is a universal virtual machine for running applications written in JavaScript, Python, Ruby, R, JVM-based languages like Java, Scala, Clojure, Kotlin, and LLVM-based languages such as C and C++.



### 热点探测

Hot Spot Detection

* 基于采样的热点探测
* 基于计数器的热点探测

![](C:/Users/Five/Desktop/note/img/20170615135255238.jpg)



[^1]:漫话：为什么Java中的main方法必须是public static void的？ - 清风徐来的文章 - 知乎 https://zhuanlan.zhihu.com/p/283389084
[^2]:https://www.jianshu.com/p/76a7ca8261c0
[^3]:JAVA类，你不可不知的main方法 - 程序员伪架师的文章 - 知乎 https://zhuanlan.zhihu.com/p/138926334
[^4]:John Aycock. 2003. A brief history of just-in-time. <i>ACM Comput. Surv.</i> 35, 2 (June 2003), 97–113. DOI:https://doi.org/10.1145/857076.857077
[^5]:https://en.wikipedia.org/wiki/Just-in-time_compilation
[^6]:https://blog.csdn.net/shengzhu1/article/details/73281722
