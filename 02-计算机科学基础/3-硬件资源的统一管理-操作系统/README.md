

> 你是否惊叹于Nginx的高并发行？是不是感觉Golang的垃圾回收器真的很垃圾？除了这样的感叹，你也许还好奇过这样一些问题：MySQL的I/O性能还能不能再提升？网络服务为什么为掉线？Redis中经典的Reactor设计模式靠什么技术支撑？Node.js的I/O模型长什么模样？

# 概述[^3]

![image-20210107193208404](C:\Users\Five\Desktop\note\img\image-20210107193208404.png)

如图所示，操作系统是软件，同时也向下管理硬件，向上承载上层软件。

操作系统还可以有多种不同的架构，但不管架构如何，其承上启下的地位不变：

![](C:/Users/Five/Desktop/note/img/OS-structure2.svg)

这种承上启下的结构主要有以下两点优势：

* 当上层软件出问题时（异常、中断等等），保护底层硬件
* 对上层应用提供简洁、统一的接口，屏蔽顶层硬件的差异

说白了大概就是解耦、规范，对上对下都好。

任何一个复杂的系统中，这样类似承上启下的结构都不少见，比如同样还是在计算机领域，有了操作系统还不够，还想要虚拟机，乃至现在逐渐成为潮流的，更统一，更规范的容器技术。

> 中间套一层承上启下（解耦）是不得已而为之，否则进一步开发的难度和成本会急剧增加，难度可能会来源于这两方面：
>
> * 底层提供商山头林立，标准得不到统一
>   * 之于计算机硬件就是Intel、AMD、ARM等等，除非逐个适配，否则顶层很难办事
>   * 当然操作系统也逐渐山头林立，随着我们的开发重心想要继续上移，POSIX和容器技术都是对OS封装的尝试。
> * 底层太过复杂，开发成本和难度过大
>   * 点名表扬Python，效率低点怎么了，鄙视链底端又怎么了，调库一行代码完事是真的香啊。
>
> 对于计算机底层而言，这两点都占了。所以操作系统的诞生顺理成章。
>
> 当然这一切还有另外的原因——硬件性能的飞速提升，使得操作系统的那点资源消耗更开发效率一比，不算啥事，不然如果硬件停留在80386那水平，哪还要得起操作系统，都滚去写汇编，不手写机器码是最后的仁慈。

总的来说，操作系统具有四个特征：并发、共享、虚拟、异步。

其中虚拟应该是最核心、最根本的部分，甚至可以说操作系统对于开发意义就是将CPU抽象（虚拟）成了进程，将内存抽象成了虚拟内存，将磁盘等I/O设备抽象（虚拟）成了文件。

> 所谓抽象（虚拟）也就是前面所说的屏蔽底层差异
>
> * 抽象出进程的概念屏蔽了CPU型号和指令集的差异
> * 抽象出虚拟内存的概念屏蔽了了地址管理的麻烦
> * 抽象出文件的概念就更猛了，直接屏蔽了各种千奇百怪的I/O设备的差异。

## 进程

![image-20210228115705759](C:\Users\Five\Desktop\note\img\image-20210228115705759.png)

当你用你的PC的时候，你往往不会是只干一件事。比如当我打出这行字的时候，可能我一边还在听歌，屏幕还是分屏的，左边是浏览器，右边是Typora，右下角的时钟依旧勤勤恳恳，wifi也不会莫名其妙突然断开……

明明只有一个CPU（不考虑多核，事实上大部分时候也都用不到多核），却能hold住这么复杂的情景，一切都井然有序，这可能很大程度要归功于进程的概念。

进程与进程之间是隔离的，所以开发者在开发自己的应用的时候，都只需要考虑自己的程序启动时的那一个进程即可，不管计算机上还运行着多少其他进程，都干扰不到自己的进程所执行的逻辑——仿佛进程独享整个计算机资源一样。

当进程让出资源的时候，则只需保存当前的处理进度（Context）即可，当再轮到当前进程的时候，重新载入Context即可继续运行。

![image-20210228162855186](C:\Users\Five\Desktop\note\img\image-20210228162855186.png)



此刻我这小破电脑上也运行着200+进程，3000+线程。

### 线程

时代总是在变的，刚开始的时候进程的notion应对大部分场景绰绰有余，随着各种高并发的网络场景，线程作为一种新的programming model愈发重要。

> 进程与进程之间资源相互隔离，（同一个进程的）线程与线程之间共享同一个进程的全部资源。

数据共享更简单、当CPU有多核时多线程能更好地利用多核的性能，这些都是进程所没有的优势。

## 虚拟内存

之前说了，进程仿佛能够独占整个计算机的资源，而存储部分，这种独占资源（与其他进程隔离）的效果就是通过虚拟内存实现的。

![image-20210228171024531](C:\Users\Five\Desktop\note\img\image-20210228171024531.png)

上图的左下角有一个0，表示图中的地址是从下往上依次增长的。

* Program code and data，地址空间的初始化过程会在第七章有详细描述。
* heap，说run-time heap会更直观一点，其大小可以通过`malloc`、`free`等C程序指令动态地伸缩。
* Shared libraries，如图所示，printf等基础函数功能放在此处，同样在第七章会有详述。
* Stack，和堆相同，可以动态伸缩，当call一个函数时候，Stack会扩张，函数return后stack会缩小。
* Kernel virtual memory，程序一般不能直接访问这部分代码，而要通过invoke内核达成操作。

## 文件

《CS：APP》原文：A file is a sequence of bytes, nothing more and nothing less.

所有的I/O设备（磁盘、键盘、显示屏、网卡）都可以视为一种文件（modeled as a file）。

开发人员可以更专注到自己应用程序的核心逻辑，而不在乎（blissfully unaware）I/O设备花里胡哨的形式，统一像文件一样读写操作即可。

（I/O设备的具体执行逻辑这种事由I/O设备的开发人员去操心，这也算是一种解耦吧）

# 简史

基本上所有教材上都有提到操作系统发展史，还分了单道批处理、多道批处理、分时系统、实时操作系统、微机操作系统等过程。

这里抛开这些分类再简要地再梳理一下一些现在常听到的操作系统。

## 编年史

远古蛮荒时代

* 1946年，基本的人工操作方式和脱机IO方式
  * 硬件背景：继ABC（阿塔纳索夫-贝瑞计算机）之后的第二台计算机、第一台通用计算机ENIAC诞生。
  * 特点：设计较粗糙，基本不能算操作系统，软硬件没有明显分离
* 20世纪50年代中期，单道、批处理系统诞生
  * 硬件背景：出现了第二代晶体管计算机，具有推广应用的价值，但仍然非常昂贵。
  * 进展：配置了监督程序（Monitor），由监督程序（大概这就是所谓的操作系统1.0？）管理一批作业。
  * 局限：I/O和CPU工作串行，使得大量CPU时间浪费在等待I/O上。
* 20世纪60年代中期，多道、批处理系统诞生
  * 硬件背景：内存越做越大，能够容纳多道程序，IBM生产了第一台小规模集成电路计算机IBM360，并为它配套了第一个多道批处理操作系统OS/360。
  * 进展：在内存中同时装有若干道程序，当A程序需要I/O时，B程序可以获得CPU资源，继续运行
  * 美中不足：作业平均周转时间长，无交互能力

![image-20210107192023211](C:\Users\Five\Desktop\note\img\image-20210107192023211.png)

> 随着成本下降、算力、存储的提升，操作系统设计的核心需求，逐渐从提高资源的利用率和系统吞吐量，转变为用户人机交互。
>
> 同时计算机使用的使用方式绕了一圈逐渐居然回到了最初的状态——一个用户独占全机，也就是Personal Computer。



随着CPU性能的提升，I/O设备日新月异，计算机也开始提出新的核心需求或者转变原来的重心，变得越来越重视交互性、实时性。新的操作系统也由此诞生：分时操作系统和实时系统。

Unix揭开了近现代（知名）操作系统发展的序章：

* 1969年，UNIX在AT&T的贝尔实验室开发。
  * "Niplexed Information and Computing Service，缩写"UNICS"，后称为"UNIX"。
  * UNIX是一个分时系统，较完善的处理机管理、存储管理、文件管理、设备管理模块。
  * 是当时已有技术的集大成之作
* 1979年，DOS发布
  * 1983年11月，微软宣布Windows，并在1985年发行
  * 2001年，经典的Windows XP发行
* 1984年，System 1.0，MacOS前身发布
  * 具有图形化界面
  * 没错，比Linux还早几年，亏我以前还以为MacOS是Linux改，原来大家都是Unix改
* 1991年Linus第一次release Linux。（比想象中年轻得多，一直以为Linux是个老古董了）
  * 全称GNU/Linux，因为Linux通常包含了GNU计划软件。
    * GNU和Linux本不是一个东西，但却在发展中彼此依赖。
    * GNU是GNU's Not Unix的递归缩写，表明不包含具著作权的Unix代码，与Linux共同掀起开源潮流。
  * 是一套免费使用和自由传播的类Unix操作系统

> Linux is a clone of the operating system Unix, written from scratch by Linus Torvalds with assistance from a loosely-knit team of hackers across the Net. It aims towards POSIX and Single UNIX Specification compliance.

新的趋势也在出现：随着网络的发展，分布式操作系统、云主机等，都逐渐焕发出生机。



## 老祖宗UNIX和新标准POSIX

> The 1960s was an era of huge, complex operating systems.   ——《CS: APP》

> Unix (/ˈjuːnɪks/; trademarked as UNIX) is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.

OS/360、Multics（Unix的团队也曾参与，后退出）、Unix，你方唱罢我登场。OS/360很成功——但我不在乎，也不想描写，直接跳到Unix。

第一版Unix是完全用机器语言写的，1973年用C重写了内核.

1994年Unix正式对外发布，由于贝尔实验室对于大学使用Unix代码的放得很宽松，所以Unix迅速在大学受到追捧。

1970s末到1980s初，伯克利分校的研究者陆续发布了Unix 4.xBSD 版本，并在其中加入了虚拟内存和互联网协议等一系列内容。与此同时，贝尔实验室也在继续更新、发布他们的新版本。

1980s，山头林立的情况愈演愈烈，不同的Unix供应商开发、维护着自己的版本，甚至为了在自己的版本中加入一些特性使得Unix之间不再兼容——某个Unix上能运行的程序放到另一个Unix版本上就无法正常运行了。

为了对抗这种趋势，IEEE提出了标准化Unix，即后来的POSIX-Portable Operating System Interface，X表示对Unix API的传承。



> 在Github上有个项目，记录了Unix的历史代码
>
> [Continuous Unix commit history from 1970 until today](https://github.com/dspinellis/unix-history-repo/tree/Research-PDP7-Snapshot-Development)



 



Unix衍生的系统：

* Solaris
  * Oracle Solaris
  * Open Solaris，唯一一个由商业版转为开源的个例。
* AIX
  * Advanced Interactive eXecutive，IBM公司所有







## DOS





## Minix和Linux

20世纪80年代，由于AT&T所有的UNIX版权的限制，荷兰的Andrew S. Tanenbaum教授决定写一个不包含任何AT&T源代码的UNIX系统，名为MINIX（即小型的UNIX），并开放全部源代码给大学教学和研究工作，Minix于2000年重新改为BSD授权，成为自由和开放源码软件，为全球注册商标。

> Linus Torvalds虽然深受Minix的启发而写出了第一版本的Linux内核，但这种启发更多的是精神上的，Linux的设计与MInix的微内核设计理念截然相反，却采用了与UNIX相似的宏内核架构。
>
> 宏内核和微内核的观念之争，从MINIX（微内核）的创始人Andrew和Linux（宏内核）的创始人Linus就开始了。



## 试图剖析

如何看待开源中国中一片唱衰鸿蒙 OS？ - 炸弹团的回答 - 知乎 https://www.zhihu.com/question/339615503/answer/788951102

> Wintel的成功：
>
> “在消费市场，到底什么功能，才是微型计算机这产品的刚需？？”
>
> 实际上，如果你能解答这个问题，你也就能解释“为什么苹果的Macintosh和乔布斯一定会失败”，同时你也就能解释“为什么IBM会逐渐失去对整个PC市场的控制权”、以及“为什么微软和intel能迅速崛起”。而这答案在今天，是被所有人认为都是“常识”的东西，那就是“兼容”。
>
> ios的成功：
>
> 一个平台赚钱（iOS），另一个平台用爱发电（塞班）（短代支付的区域性是大坑），换了你作为开发者，你怎么选？
>
> 所以，iOS上，好的应用程序越来越多，形成正向循环（标准的马太效应）
>
> Android的成功：
>
> 简要来说，安卓的商业模式就是“用免费的技术换免费的流量”。谷歌提供给全球手机厂商免费的可定制化操作系统，而全球的手机厂商通过内置Google全家桶给谷歌提供巨大的免费流量。
>
> 在谷歌看来，Google Play Store，并不是一个应用商店，而是一个搜索引擎。在谷歌看来，这些移动端流量，最终都能套入谷歌那套“搜索-广告-变现”的变现模式当中。
>
> 如果不是有这样的商业模式支撑，是没有哪个公司愿意花巨大的成本，去给第三方手机厂商做一个“纯免费”的操作系统的。那不是商业公司干的事儿，那是公益。
>
> ……
>
> **操作系统的成功，从来都是“商业模式创新”的产物，技术创新从来不是驱动力，技术只是商业模式的支撑。**
>
> （作为一个工科生觉得有被冒犯到，但雀石言之有理）

> 网景浏览器为什么做不过IE浏览器？IE浏览器为什么做不过Chrome浏览器？
>
> 微软的商业模式是买操作系统送IE浏览器。而网景的商业模式是拿浏览器当软件卖。
>
> 卖操作送浏览器的模式，对微软来说，是没有足够研发动力的，因为不赚钱。但是对于Chrome的开发者谷歌可不一样，当一个用户使用Chrome浏览器的时候，他的“搜索流量”将全部导入Google网站上。这意味着，只有有Chrome浏览器的装机量，Google就多一份搜索流量。而对一个搜索引擎来说，只要有“搜索流量”就，有广告就有收益。所以，这意味着，Chrome浏览器的质量好坏，直接关系到Google广告收益的高低，对企业来说，那研发动力就大大不同了。





# 主流内核和操作系统

* Linux
* Zircon
* NT内核

## OS kernel架构之争

> The kernel is the portion of the operating system code that is always resident in memory. When and application program requires some actions by the operating system, such as to read or write a file, it executes a special system call instruction, transferring control to the kernel.
>
> Note that the kernel is not a separate process. Instead, it is a collection of code and data structure that the system uses to manage all the process.
>
> ——《CS: APP》

![image-20210107194009481](C:\Users\Five\Desktop\note\img\image-20210107194009481.png)



与企业管理相类比[^1]：

宏内核类似于大量的高层/管理层：管理层直接自己负责大部分的事务，雷厉风行，但公司的管理、运行、决策可能会混乱。

微内核类似于少量的高层/管理层：管理层只负责核心的内容，但因此导致管理层和普通员工需要大量交接，耗时耗力。

> 对于小公司，往往前者的效率更为可贵。
>
> 而对于大公司，往往后者的可管理性更为可贵。

如果顺着类比看操作系统发展，有理由相信未来是属于微内核的。（不过类比毕竟仅供参考，不好过度解读）

参考wikipedia上一张更经典、详细的图：

![](C:/Users/Five/Desktop/note/img/OS-structure2.svg)



更多关于微内核的内容推荐阅读标注的参考文献[^2]。



更极端的还有“外核”exokernel的架构

将操作系统分为两部分，一部分跟硬件打交道，另一部分libOS跟具体应用打交道，libOS通过和Exokernel打交道来访问硬件。



当然还有VMM，Virtual Machine Monitor，虚拟出一个完整的计算机。也算是一种特殊的操作系统。

> 以前总在想虚拟机终究没有物理实体支撑，真的能模拟出跟实际操作系统体验一样的环境吗？
>
> 但现在想想，其实操作系统提供的也都是虚拟出来的资源，操作系统能给的，虚拟机自然也应该能给，能在正常操作系统上跑的，自然也该能在虚拟机承载的操作系统上跑。



# 其他



> 操作系统是一个死知识横行的领域。很多人发现操作系统课难学，难理解。里面有些内容，比如各种同步机制，很多人上完课毕了业，工作很多年以后都还弄不明白是怎么回事，它们为什么在那里。类似的东西包括虚拟内存，进程与线程的区别，等等。
>
> 经过了很多的经验和思考，加上其他领域给我的启发，我终于明白了。原来很多这些概念都是无须有的，死掉的知识。[^4]

我当然不敢像王垠大佬这样去认为，也不认为自己的水平足够做到看透本质、一力降十会，但参考一下还是敢的。



> 操作系统课程里面的概念经常是这样形成的：[^4]
>
> 1. 很久以前，有人为了解决了一个特定的问题，提出了一个概念（比如 semaphore）。这个概念本来只有一个用途，就是解决他遇到的那个特定的问题。
> 2. 因为这人太有名，这概念就被写进了教科书里。有时候连他当时的具体实现细节都给写进去了。比如 semaphore 的两个操作被叫做 P 和 V，连这两个名字都给作为“典故”写进去了。
> 3. 教授们照本宣科，吹毛求疵，要你用这概念解决很多其它问题。很多根本就是人为造出来的变态问题，现实中遇不到的，或者是一些不该用这个概念解决的问题。



[^1]:bilibili 王道考研 操作系统 https://www.bilibili.com/video/BV1YE411D7nH?p=5
[^2]: 什么是微内核？ - linux阅码场的回答 - 知乎 https://www.zhihu.com/question/339638625/answer/1148196893
[^3]:《Computer System: A Programmer's Perspective》
[^4]:《关于微内核的对话》王垠 http://www.yinwang.org/blog-cn/2019/08/19/microkernel
[^5]:《一种新的操作系统设计》 王垠 http://www.yinwang.org/blog-cn/2013/04/14/os-design
[^6]:极客时间《操作系统实战45讲》