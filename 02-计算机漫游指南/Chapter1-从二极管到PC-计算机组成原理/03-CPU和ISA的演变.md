# 指令集架构ISA

## 处理器和指令集的关系

处理器架构是用硬件电路去实现指令集。具体用怎样的处理器，怎样设计硬件电路，都可以有不同。

所以是指令集决定了处理器的架构，即先有指令集，后有围绕指令集设计的底层硬件和上层软件。



> 从耦合的角度来讲也应该是上层的软件和底层的硬件都去依赖/耦合指令集这一统一规范。而不是让指令集向下去耦合硬件。
>
> 这样最终达到的效果就是通过指令集解耦底层硬件和上层的软件代码。



汇编语言是用人类看得懂的语言来描述指令集。否则指令集就只是一堆二进制机器码。

不过汇编和机器码一一对应，所以常用汇编表示指令集。



## 指令集发展史

* 1978年6月8日，Intel发布8086，同时带来x86指令集IA-16
  * 1985年，Intel推出的80386微处理器中首先采用IA-32
  * 2004年，Intel推出了自己的64位版x86，即EM64T/x86_64
* 

> Intel试图开发不兼容IA-32/x86_32的全新体系IA-64，而AMD在IA-32的基础上，开发了兼容IA-32的AMD64。
>
> Intel被微软一顿忽悠，说好了会基于IA-64重新开发操作系统，结果就硬鸽，只有基于AMD64的windows操作系统。
>
> IA-64，卒。Intel也不甘心地转向AMD64（交叉授权），但总不能叫这个名呀，多糟心，那就叫x86-64，在代码里变量名不能用-，遂习惯用x86_64。
>
> Wintel友谊的小船说翻就翻。



## x86指令集

x86指令集是商业上最为成功、影响力最大的体系结构

![image-20201002153429076](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-31.png)

> x86指令集是一种变长的指令集。
>
> 可能不同指令使用频率的差距的确到了要用哈夫曼编码的地步？

### 简单的x86指令集示例

* 运算类指令
  * 算术运算和逻辑运算
  * 操作的对象主要是通用寄存器

![image-20201002181828141](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-37.png)

INC指令，只有一个字节，对操作数自增1

> 从INC中看x86的设计思想
>
> INC这种指令，你说它突兀吗，突兀，毕竟只是加法的一种特例，没有也无伤大雅。
>
> 但程序中用到的多吗？很多。所以x86为程序中常见的情况专门设计指令，更计较存储空间，而不是逻辑简洁。

ADC指令，带进位加法，即会把上一次计算后可能产生的进位带进来。

当进行32位以上运算时，要求低位字节相加，而高位字节再相加时就要考虑低位相加的进位，即CF，这时就要用到ADC指令

> 很显然最低位那段用`add`（别让上一个指令的遗留影响这个指令的执行），其他的用`adc`，最终拼接出结果。



* 传送类指令
  * 从存储器都通用寄存器，从寄存器到I/O接口等
  * 操作对象涉及大部分寄存器

![image-20201002160150951](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-34.png)



对于具体的MOV指令：

> 若直接给出操作数，则操作数会体现在指令编码中，CPU在取值的时候会把40作为指令编码的一部分取回。
>
> 直接给操作数不加[]，地址加[]



> 汇编语言中的中括号[]有点类似于C语言中的指针概念的*运算。
>
> 即加了括号表示给定值是一个指针，需要取它的值，而不是它本身。

![image-20201002162411688](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-35.png)

MOV指令编码：

![image-20201002180726289](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-36.png)

其中，第一条“MOV AX, 10EEH”中，1011代表立即数类型的MOV指令，000代表寄存器编号AX，后两个字节表示立即数10EEH.

第二条中……不好意思，汇编知识储备不足，不太清楚具体细节，先留白，以后如果还能记得再来补充。



* 转移类指令
  * 改变指令执行顺序
  * 操作对象主要是指令指针寄存器和段寄存器

![image-20201002184434197](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-38.png)

![image-20201002184701294](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-39.png)

![image-20201002184813012](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-40.png)



* 控制类指令
  * 暂停处理器、清楚标志位
  * 操作对象主要是标志位

![image-20201002184957302](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-41.png)

### 程序示例

![image-20201002160003433](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-33.png)

可以尝试在寄存器尺度一步一步地复现程序过程。

### 复杂的x86指令举例

* 串操作指令
  * 对存储器中的数据串进行每次一个元素的操作
    * 串的基本单位是字节或字
    * 串长度可达64KB
  * 共5条串操作指令
    * 3种重复前缀。

![image-20201002185516007](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-42.png)



> 不是没有操作数，而是操作数太多了
>
> 隐含操作数：
>
> 源串地址为DS:SI，目的串地址ES:DI
>
> 串的长度在CX寄存器中

> 隐含操作（硬件自动完成）
>
> 修改SI和DI，指向下一个串元素
>
> 若使用重复前缀，CX=CX-1

![image-20201002190802698](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-43.png)

标志寄存器中的DF标志位表示串传送方向。

DF=0，从低地址开始传送，SI和DI自动增量修改；DF=1，从高地址开始传送，SI和DI自动减量修改。

方向标志的作用如下图所示，我只能说——妙啊。![image-20201002191227977](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-44.png)



![image-20201002191352257](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-45.png)

> IA架构的思想于软件工程的想法似乎正好想法。
>
> IA通过大量的指令，使得大部分实践中用到的操作（哪怕看上去不该是原子操作）都有对应的单独指令（而不需要自己通过组合一堆指令实现）。
>
> 当然可能有一定的方便，代码明显会更短，却也带来指令集和逻辑的复杂性。
>
> 虽然代码更短符合软件工程的想法，但以复杂度为代价是软件工程不能接受的。
>
> 而MIPS，在与IA相反的设计理念下，生根发芽。



### x86之IA-16

#### IA-16特点

* 内部的通用寄存器为16位
  * 兼容8位数据
* 对外有16根数据线和20根地址线
  * 寻址空间为$2^{20}字节=1M$

> 看到这里会稍微有点疑问，地址总线位宽比通用寄存器长，那岂不是要两个寄存器去表示一个地址？

确实。X86有特殊的访问地址生成方式。

用段寄存器的方式（Code/Data/Extra/Stack Segment），与其他寄存器联合生成存储器地址。

即如下图所示，物理地址 = 段基值<<4 + 偏移量。

![image-20201002150556130](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-29.png)

> 那问题又来了，那怎么知道此时该选择哪个段寄存器呢？



> 还有tm的用两个16寄存器共同表示一个32位寄存器它不香吗？少用三个寄存器，寻址空间还直接上升到4G。
>
> 16位寄存器和32位寄存器技术差距那么大的吗？



* 物理地址采用“段+偏移”的方式



#### 8086寄存器模型

（能截图何必手打）

![image-20201002144311484](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-24.png)



关于寄存器的具体描述

* 数据寄存器

![image-20201002144416065](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-25.png)

补充：

SP: Stack Pointer

BP: Base Pointer

SI: Source Index

DI: Destination Index



* 标志寄存器

![image-20201002144834978](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-26.png)

![image-20201002145515264](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-27.png)



* 指令指针寄存器

但16位寄存器的所能表示的寻址空间即使在那个时代都被嫌弃小了

所以需要20根数据线，并用段+偏移量的地址表示方法。

![image-20201002145901676](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-28.png)



### X86之IA-32

#### IA-32特点

* 第一款32位微处理器
* 支持32位的算术和逻辑运算，提供32位通用寄存器
* 地址总线32位，4G内存空间
* 改进了保护模式
* 增加了虚拟8086模式，可以同时模拟多个8086微处理器

> 1978年退出8086，1985年推出80386。



#### 从8086扩展而来的寄存器模型

![image-20201002152958638](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-30.png)

### X86之x86-64

> x86-16/32和IA_16/32通常指的是同一个东西，但x86-64和IA-64不是。



#### x86-64寄存器模型

![image-20201002154730402](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-32.png)



## MIPS指令集

MIPS（Microprocessor without Interlocked Piped Stages），RISC指令集的代表，国内龙芯采用的架构，其专利期已过，可免费使用。

![image-20201002192314437](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-46.png)



### 主要特点

* 关注点
  * 减少指令的类型
  * 降低指令的复杂度
  * A simpler CPU is a faster CPU

* 固定的指令长度
  * 32bit，1word（与x86中16bit一个word不同）
  * 简化了取指操作
* 简单的寻址模式
* 指令数量少，指令功能简单
* 只有Load和Store两条指令访问存储器
  * 不同于x86指令ADD等操作可以直接访问存储器



虽然逻辑和结构简单了，但直接用基础、简单的指令进行编程，程序的体积会更大。



### MIPS指令集架构概述

> 关于MIPS32指令集的官方文档可在我博客主页的appendix目录下找到。或可官网获取。
>
> 以下内容取自《MIPS32™ Architecture For Programmers Volume II: The MIPS32™ Instruction Set》





### MIPS指令集

![image-20201002200434263](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-51.png)

R型指令

![image-20201002200737624](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-53.png)

* rs，Resource Register 通常为第一个源操作数
* rt，Target Register 通常为第二个源操作数
* rd，Destination Register 通常为目的操作数
* shamt，Shift Amount 移位指令进行移位的位数

![image-20201002201415955](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-54.png)



----

I型指令

![image-20201002201531173](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-55.png)

> x86指令可以随意使用更大宽度的立即数，指令没有限制长度。
>
> 但MIPS不行。

![image-20201002202323857](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-56.png)



* 条件分支指令

![image-20201002202506636](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-57.png)

示例：

![image-20201002202647281](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-58.png)

局限性

![image-20201002202853920](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-59.png)



----

J型命令



![image-20201002205601931](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-61.png)

![image-20201002204019858](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-60.png)



----

前文描述指令集是按R/I/J型划分，没有像x86一样通过运算、访存、分支进行划分。下图是对后一种划分的补充。

![image-20201002200501393](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-52.png)



### MIPS寄存器

通用寄存器

![image-20201002200103594](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-49.png)

![image-20201002200204936](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-50.png)



> 没有标志寄存器

## 其他指令集

### ARM

ARM在平常提及时可能指两样不同的东西：

* 英国Acorn公司设计的RISC微处理器，Acorn RISC Machine
* Acorn公司和Apple合作创立的ARM公司，Advanced RISC Machine，半导体知识产权提供商

一个是ISA，一个是公司。此处指前者。

ARM公司顶着Intel逆风飞翔也是传奇，它在世界范围有超过100个的合作伙伴。ARM 采用转让许可证制度，自己不制造芯片，只将芯片的设计方案授权给其他公司，由它们来生产。

### RISC-V



### SPARC, POWER

SPARC（Scalable Processor ARChitecture）架构完全开放





## 一个简单的计算指令系统

### 指令类型

* 运算类指令
  * ADD R, M：将寄存器R中内容与内存M中对应内容相加，保存到R

* 传送类指令
  * LOAD R,M：M中内容装入R
  * STORE M,R：将R中内容存入M

* 转移类指令
  * JMP L：无条件转向L处



### 指令的格式

> CPU硬件和软件沟通的桥梁

* 每条指令等长，均为2个字节
* 第一个字节的高四位是操作码 ，低四位是寄存器号
  * 如LOAD: 0000, ADD: 0001, STORE: 0010, JMP: 0011
    * CPU如何识别指令可参考之前的文章
    * 其中JMP是对寄存器PC操作的指令
    * LOAD、ADD、STORE等指令主要涉及其他的寄存器，这个过程中寄存器PC通常递增寻找下一条指令。
  * 四位寄存器号意味着最多可表示$2^4=16$个寄存器
* 第二个字节表示存储单元地址
  * 最大可以对应$2^8=256$个地址，即可以使用256字节的存储器



### 指令实例

* 存储器中M1，M2两个地址的内容相加并存入地址M3
  * 其中地址M1=5，M2=6，M3=7

（没错，汇编也配拥有语法高亮）

![image-20201002125151225](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-22.png)

![image-20201002125556953](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-23.png)



> 程序如何开始？

在寄存器PC中载入程序的第一字节的所在地址0000 1000。

然后如指令操作实例所示，PC寄存器递增，执行完所有指令。

> 那PC寄存器怎么载入第一条0000 1000呢？

这其实是不一定的，一般计算机重启复位后，PC寄存器的初始数值需要软硬件双方商量好。

很多时候PC寄存器初始设置为0000 0000，那么这时候只需要在0000 0000处写一条指令JUMP 0000 1000，令PC寄存器无条件跳转到这段程序的第一行即可。



# 处理器



## 处理器编年史

显然，指令体系架构是处理器的一部分，是处理器的软件设计，所以不妨先梳理一下处理器的发展史。

> 一直说x86，x86到底指哪些？现在的CPU还是X86吗？

下图是我的PC，其System type是x64-based，即x86_64架构。

![image-20201016124028668](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016124028668.png)



此处仅列出intel的部分作为参考。

* 1971年，Intel 4004（在之前的文章中有出现4004的图），第一个能被叫做处理器的东西
* 1985年，Intel 80386，还带来了IA-32架构
* 1997年，Pentium MMX处理器，
* 二十世纪初奔腾四时代来临，AMD和Intel在开启主频大战
* 奔四之后，英特尔又推出了一种全新的系列——core系列。从它进入市场开始定位就是主流性能
  * 从这里开始英特尔更多把精力投入到改进制程和架构上

