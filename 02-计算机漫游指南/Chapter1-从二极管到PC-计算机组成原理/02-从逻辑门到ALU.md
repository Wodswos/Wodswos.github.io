如标题“从逻辑电路到通用计算机结构”，本文是关于[Coursera](https://www.coursera.org/learn/jisuanji-zucheng/home)课程和如下问题的整理：

* CPU是怎么用逻辑电路实现算数运算的？
* 现代计算机（PC）的组成是怎么样的？

主要参考内容：

[Coursera](https://www.coursera.org/learn/jisuanji-zucheng/home)课程

[知乎高赞回答](https://www.zhihu.com/question/348237008)

# 算术运算

## 加减法实现

### 简单的加法器

![image-20201006192111868](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006192111868.png)

用一个异或门得到当前位结果S，用一个与门得到进位C。

> 当且仅当其中一个为0，一个为1当前位和为1，对应逻辑关系异或
>
> 当且仅当两个加数都为1时进位为真，对应逻辑关系与



但半加器能得到进位，却不能计算进位。因此需要将两个半加器组合，得到一个全加器。

即第一个半加器负责当前位的加法，第二关半加器负责处理可能存在的进位。最终的得到总的结果。

![image-20201006192405053](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006192405053.png)



进一步，多个1-bit Full Adder串行，就形成了简单但完整的加法器。

![image-20201006192427460](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006192427460.png)

同理可构建16、32位加法器。



### 异常处理：溢出和进位

在硬件层面，并不在乎有符号数和无符号数的区别。

![image-20201006192915671](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006192915671.png)

![image-20201006192849978](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006192849978.png)

“进位”是很好判断的，毕竟有标志位可以参考，计算机很容易发现这类错误。



![image-20201006193242110](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006193242110.png)

* MIPS对溢出的处理方式

![image-20201006193342573](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006193342573.png)



### 减法运算

#### 补码

对于计算机而言，减法是加法的特殊形式，即加一个负数，或者说就是有符号数的运算。

而这个负数，可以通过对其绝对值进行补码规则处理得到。

> 补码规则：按位取反，末尾加一

所以$A-B=A+(-B)=A+(\bar B + 1)$



#### 减法运算实例

![image-20201006193608328](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006193608328.png)



### 加法器优化——超前进位

#### RCA的关键路径长度

![image-20201006193809445](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006193809445.png)



![image-20201006194024706](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194024706.png)

#### 提前计算进位输出信号

![image-20201006194139889](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194139889.png)

![image-20201006194345166](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194345166.png)

![image-20201006194505011](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194505011.png)

![image-20201006194530818](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194530818.png)



![image-20201006194617601](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006194617601.png)



## 乘除法的实现

### 从十进制到二进制

> ENIAC采用十进制，EDVAC采用二进制，两者电路的复杂度有巨大的差别。
>
> 《EDVAC的报告草案》：
>
> 1. 电子管是一种“全或无”的设备，适合表示只有两个数值的系统，即二进制。
> 2. 二进制可以大幅简化乘法和除法的运算过程，不再十进制乘法表，也不再需要两轮加法。
> 3. 但十进制更适合人使用，所以输入输出设备应当承担二进制和十进制的转换工作。

![image-20201016162226769](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016162226769.png)

#### 运算过程的调整

寄存器是有限的，不能（或者说不太好）像纸面运算一样同时保留那么多的中间结果。

所以需要对运算过程进行调整：

1. 将乘积初始值设为0
2. 每产生一个中间结果，直接将其累加到乘积上



### 乘法器的实现

![image-20201016175648385](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016175648385.png)

其中Multiplicand表示第一个乘数（或称被乘数），Multiplier表示第二个乘数

1. 若Multiplier当前最低位为1，则Product+=Multiplicand
2. multiplier>>1并补0, Multiplicand<<1并补0
3. 若Multiplier全为0（或循环次数=Multiplier位数），运算结束，否则回到步骤1循环

![image-20201016175526371](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016175526371.png)

流程图如下所示（我也想用markdown画一下，但是mermaid的流程图确实有点丑，flow又有点繁琐，就直接贴截图了）：

![image-20201016175720056](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016175720056.png)



以下内容为个人的叨叨，可以跳过。

> 可以注意到，其实在乘法运算中并没有“乘法”，只有移位和加法两种操作。
>
> 或者换个角度说，我们很容易发现，对于乘2，只需左移一位，低位补0即可（所以C++/Java中乘2、4等操作往往推荐使用位运算<<），同样，对$2^n$乘法都是仅需左移n位。
>
> 那乘3这种呢？很简单，用左移1次的数+左移0次的数。
>
> 那乘n呢？只需将n拆分成$k_02^0+k_12^1+...+k_m2^{m}$的形式，显然$k_i\in{0,1}$，若$k_i$为1，则总乘积加上左移$i$次的数，最后累加的就是结果。
>
> 这些$k_0,k1,...,k_m$反向排列起来$k_m..k_1k_0$是什么呢？其实就是另一个乘数的二进制。
>
> 绕了那么大弯，算是对乘法器的另一种理解角度。只想借此说明乘法是移位和加法的结合，或者不准确的说，移位才是计算机乘法（或者说快速完成乘法）的核心。
>
> 不然粗暴地算，乘N就是累加N次，那不是要累死？位移直接使得计算复杂度取了对数，即累加次数变为了N的二进制数的位宽。



### 乘法器优化

#### 可以并行的计算

对于最原始的乘法器，计算一个32位的乘法需要约100个时钟周期。

> 时钟上升沿到来之前，寄存器内容不会发生变化

乘数寄存器右移、被乘数寄存器左移、乘积寄存器保存ALU计算结果三步操作可在同一个时钟周期内并行完成。

![image-20201016181848643](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016181848643.png)



#### 减少不必要的硬件资源

> 看这部分优化的感受是：的确是非常抠了……

* 被乘数占用的位宽=被乘数位宽+乘数位宽，而不是被乘数的有效位宽，存在冗余
* 乘数寄存器占用的位宽会随运算进行右移而减少，但没能被利用
* 乘积寄存器初始存在与被乘数占用位宽类似的问题，即刚开始不需要那么多位宽
* 加法器实际参与运算的是4位而不是8位（以1000*1001为例）

对应优化方案

* 去掉被乘数左移的功能，使之固定位置，从而也固定位宽，还省了左移的过程
  * 但会产生ALU两个加数对齐的问题
* 直接取消乘数寄存器
  * 乘数放哪里呢？
* 对乘积寄存器不做删减
  * 但需要增加功能解决前两个寄存器优化的问题，能力越大，责任越大嘛
    * 解决被乘数左移功能删减带来的对齐问题——被乘数不左移，让乘积右移
    * 放置乘数，初始置于乘积寄存器的低四位
* 乘积寄存器只有高四位参与运算，被乘数也只有四位，所以只需要四位加法器

![image-20201016185719705](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016185719705.png)

同样可以推广到N位的乘法器：

![image-20201016185803585](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016185803585.png)



### 除法运算

#### 带余数的除法器

![image-20201016194224115](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016194224115.png)

![image-20201016195330026](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016195330026.png)

当然，在日常中我们可以直接比较大小，决定是否要减去除数，而不用在减完之后回退。

但在计算机中，大小的比较恰恰就是通过减法结果的正负来实现。



![image-20201016201345177](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016201345177.png)

#### 除法器的优化

* 与乘法器相似，去除商寄存器、除数寄存器的移位，让余数寄存器去实现
  * 余数寄存器只有高32bit参与加减法运算
  * 将商放入余数寄存器的低位
    * 计算结束后高32位为余数，低32位为商

![image-20201016202147466](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016202147466.png)







> 关于浮点数
>
> 在十进制中，小数可以视为$k_1*10^{-1}+k_2*10^{-2}+...+k_n*10^{-n},k_i\in\{0,1,2,..,9\}$
>
> 同理，小数在二进制中也可以视为$k_1*2^{-1}+k_2*2^{-2}+...+k_n*2^{-n},k_i\in\{0,1\}$
>
> 当然，在十进制中的有限小数比如0.3，在二进制中就不能被精确表示了，而是一个无限循环小数，形如$0.0\dot100\dot1$。（天可怜见，初中的知识我应该没记错）
>
> 这也是为啥浮点数保存一个确切的十进制都会丢失部分数据的原因了，二进制人家真的做不到啊！当然不是真的不行，可以通过BCD编码等方法实现。
>
> 但二进制能精确表示，十进制都能精确表示，毕竟$2^{-n}$在十进制中都是有限小数。（三进制里能精确表示的十进制就hold不住了，$3^{-n}$不是有限小数。）





## 最原始暴力的编程

至此，我们已经能够进行简单的四则运算了，但是具体的某个电路似乎只能执行某个特定的算术逻辑，比如对于如下算式：

```
(A + B) * 2
```

我们需要设计如下一个电路：



那如果变成了下式

```text
(A * 2) + B
```

那该怎么办呢？再造一个电路吗？

答案就是编程——改加法器模块和位移模块的接线（如图），改成输入A先过位移模块，再进加法器。

![](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-07.jpg)

虽然妹子很好看，但插线属实太繁琐了，能不能让Computer明白我们的意思自己做出调整呢？当然可以。

> 冯·诺依曼《关于EDVAC的报告草案》：
>
> ENIAC的开关定位和转插线只不过代表着一些数字信息，完全可以像程序管理的数据一样，存放于主存储器中。

具体的实现便是多选器。



# CPU的理解和记忆

## 多选器

![image-20201006191709581](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006191709581.png)

如上图所示，当多选器为输入为00时，会最终输出第一个与运算模块的计算结果；当多选器的输入为01时，就会选择输出第二个或运算模块的计算结果。

若有更多的模块，则可以引入更多bit，用n个bit控制$2^n$个输入的选择。

![](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-10.jpg)



通过选择器可以设计激活针脚，这个激活针脚输入1则激活这个模块，输入0则不激活。

这样我们就能通过指令控制数据流入哪个模块，而不是通过繁琐的插线了。



> 当然，我们还漏了一个重要的问题，计算机每次进行算数运算的中间结果该怎么被保存呢？
>
> 我们知道，算数运算的本质是逻辑电路，而逻辑电路的输入输出是高低电平（代表1和0），那这些高低电平从哪里来？又到哪里去（被保存）？我们打开自己的PC的时候可不会去手调电路吧？

## 寄存器

### 原理：触发器

![](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/1-08.jpg)

上图所示结构即为触发器，**触发器能够存储1bit的信息！**

> 话说高中的时候通用技术课还学过这个电路，当时就觉得这玩意整这么复杂有P用，花里胡哨的。哎，真香。

两个与非门+两个非门构成。即如下逻辑
$$
Q = \overline{\bar{S}\and \bar{Q}} = \bar{\bar{S}} \or \bar{\bar Q} = S \or Q
$$

$$
\bar{Q} = \overline{\bar{R}\and Q} = \bar{\bar{R}} \or \bar Q = R \or \bar Q
$$

S是Set，即给S通入高电平，则$\bar S=0$ ，通过与非门（与门有0则0，与非门有0则1）触发Q，使之为1。

R是Reset，即Q为1时，R通高电平过非门后为$\bar{R}=0$，会使与非门输入$(1,1)\rightarrow(1,0)$，进而触发$\bar{Q}=1$，此时$S=0,\bar{S}=1$，与非门输入$(1,1)$，Q输出为0。

Q即为存储的那个比特。当S和R均没有通高电平时Q的状态不会改变。

### CPU时钟

因为要透彻理解寄存器，似乎离不开CPU时钟的概念，所以……

> 害，怎么说呢，作为一个软件工程专业的学生，没有数字电路的基础，就是四处碰壁。
>
> 理解不一定正确，只能将就看。

先转载点题外话，感觉太tm真实了，但刨根问底还挺快乐的。

[一个执着于刨根问底的软工狗是没有好下场的](https://www.zhihu.com/question/53019975)

> 起初，你困惑于时钟。你对自己说： 是不懂数字电路
>
> 然后你会想 产生时钟的振荡电路 是什么原理。你觉得不踏实，你对自己说：嗯，应该去学一下模电。
>
> 然后你会想 NPN PNP 是什么原理，为什么能造出三极管什么的。你觉得不踏实，你对自己说：嗯，应该去学量子力学，物理知识。
>
> 然后你进入量子力学的世界，你发现数学能力捉急，之前理解的世界都是实数，没有维度概念，你觉得不踏实。你对自己说：嗯，应该增加数学修养。
>
> 然后你进入数学的世界，打好数学基础，然后苦恼于为何1+1=2 为何概率和等于1 久久不能释怀，你觉得不踏实。 你对自己说：嗯，应该进一步思考数学的本源。
>
> 然后你进入更高级的数学世界，思考公理化，然后苦恼于天分有限，已经一把年纪了。
>
> 这个时候你身边会你之前非常不屑的摆弄php js的小伙伴们已经搞起了自己的startup 拿到了风投 拥抱白富美走向人生巅峰了。
>
> 都是时钟惹的祸
>
> 
>
> 作者：FancyRush
> 链接：https://www.zhihu.com/question/53019975/answer/133207084
> 来源：知乎
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



同样是在这个知乎问题下看到的一个对该问题的评论，不太好标转载信息，就直接贴内容了，感觉有借鉴意义。

> 对于数电，你只需要知道组合逻辑就是玩与或非、时序逻辑在玩触发器触发器，了解触发器和与或非是啥。然后记住，时序电路必须有时钟才能工作。
>
> 对于模电，你只需知道数字电路的元件都是用模拟电路设计出来的，高电平1，低电平0。晶振利用晶体的压电效应产生交流电，就是01交替的时钟信号供那些时序电路使用。
>
> 至此您就明白了晶体产生时钟信号，驱动时序电路，和组合电路一同构成CPU，它可以执行特定的指令，即运行软件。OK。再往下，就是电子元件和物理知识。这一切建立在经典电磁学和量子物理学的基础上。

其实吧，作为一个分流大数据方向的软工狗，时钟对我还是有很多思考意义的。在分布式处理中最典型的一个问题就是没有中央时钟，很难判断两个异地任务的先后顺序。



以下正文：

硬件电路有两种，组合电路和时序电路，只有时序电路有记忆功能，也只有这样

而时序电路的实现，需要时钟进行统一协调

> 从某种程度上来说，时序电路算是有限状态自动机？
>
> 所以时钟频率就是自动机的转换频率？



时钟不是作用在ALU上，而是作用在寄存器上。



### 真实的寄存器工作过程

![image-20201006190414612](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006190414612.png)

![image-20201006190513455](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006190513455.png)

![image-20201006191026791](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006191026791.png)

至此，数据就能被保存在CPU中了。



## 设计一个自己的小CPU

![image-20201006191849297](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201006191849297.png)

* 硬件设计

8个输入针脚，其中4位指令，4位数据。

* 软件设计——三个指令
  * 0100，数据读入寄存器
  * 0001，数据与寄存器相加，结果保存到寄存器
  * 0010，寄存器数据向左位移一位，即乘2

让指令输入的第二、第三、第四个针脚分别连接寄存器、位移模块和加法模块的激活针脚。

（此时输入指令的利用率是不是太低了点，每一bit只能对应一个模块，而不是每个数对应一个模块）



> CPU为什么能看懂这些二进制数？

因为CPU内部的线就是这么接的，输入的二进制数像开关一样激活若干对应的模块&改变这些模块的连通方式。



> CPU里面可能有成千上万个小模块，一个32位/64位的指令能控制那么多吗？

我们举例子的CPU里面只有3个模块，就直接接了。真正的CPU里会有一个解码器（decoder），把指令翻译成需要的形式。



> 输入指令0011会怎么样？

当然是同时激活了加法器和位移器从而产生不可预料的后果，简单的说因为你使用了没有设计的指令，所以后果自负呗。（在真正的CPU上这么干大概率就是崩溃呗，当然肯定会有各种保护性的设计，死也就死当前进程）



> 【0001，数据与寄存器相加，结果保存到寄存器】
>
> 这个一步实际上做不出来，毕竟还有一个回写的过程。我们设计的简易CPU执行一个指令差不多得三步，读取指令，执行指令，写寄存器。
>
> 经典的RISC设计则是分5步：读取指令(IF)，解码指令(ID)，执行指令(EX)，内存操作(MEM)，写寄存器(WB)。
>
> 平常用的x86的CPU有的指令可能要分将近20个步骤。



```text
0100 0001 ;寄存器存入1
0001 0100 ;寄存器的数字加4
0010 0000 ;乘2
0001 0011 ;再加三
```


