从PC加电开始，PC是怎样一步一步跑起来的？

> 按下开机键后，到熟悉的操作系统欢迎界面，计算机经历了什么？
>
> 哪个男孩能拒绝这么有趣的问题呢？

本部分简单来说：

1. CPU从ROM读取BIOS
2. 运行BIOS从磁盘的MBR（主引导扇区）读取主引导记录
3. 读取活动分区的引导扇区的引导扇区代码
4. 引导扇区代码读取加载程序。
5. 加载程序加载OS。

> 这个阶段另一个显著特点就是：还轮不到操作系统接管硬件，我们可以、也确实需要直接和硬件打交道。

![image-20201014150420718](C:/Users/Five/Desktop/note/img/image-20201014150420718.png)

# BIOS：0xC0000-0XFFFFF[^3]

BIOS，Basic Input Output System，一种业界标准的固件接口。

BIOS的内容保存在ROM（Read-Only-Memory）中，断电内容不消失，信息一旦写入就固定。



在BIOS阶段主要有如下过程和工作

1. 硬件自检POST（Power on Self Test）
2. 检测系统中内存和显卡等关键部件的存在和工作状态
3. 查找并执行显卡等接口卡BIOS，进行
4. 执行系统BIOS，进行系统检测

   1. 检测和配置系统中安装的即插即用设备
5. 更新CMOS中的扩展系统配置数据ESCD
6. 按指定启动顺序从软盘/硬盘/光驱启动
   1. 所以当重装操作系统的时候，就要在BIOS修改启动顺序。



BIOS还向操作系统提供一些系统参数，系统硬件的变化由BIOS隐藏，程序使用BIOS功能而不是直接控制硬件。（咋听着那么像操作系统原型呢）

> 现代操作系统会忽略BIOS提供的抽象层并直接控制硬件组件。

## 实模式和内存映射

实模式下最多支持1M的寻址空间。

> 下图出处[^3]：全网最硬核讲解计算机的启动过程 - 闪客sun的文章 - 知乎 https://zhuanlan.zhihu.com/p/113536449

![](C:/Users/Five/Desktop/note/img/v2-e38a4fe1280d595a25485af933ba9db3_r.jpg)

寻址的对象不止有内存——还可以是显存等外设，此时需要在地址范围中划分出一片片的区域。

> 为了实现一些快速的游戏动画效果，或者播放高码率的电影，不直接访问显存是很困难的。
>
> 于是就有设计者决定把显存映射到处理器可以（较为）直接访问的地址空间，即内存中。[^4]



* 由于历史原因，所有PC的显卡在加电自检之后会把自己初始化到80×25的文本模式。[^4]
  * 即2000个字符，对应0xB8000~0xBFFFF这段地址





![image-20201011215603177](C:/Users/Five/Desktop/note/img/image-20201011215603177.png)

## BIOS加载运行[^3]

### 强扭的西瓜

BIOS内的信息被映射到了内存0xC0000-0xFFFFF的位置，最为关键的系统BIOS被映射到了0xF0000-0xFFFFF的位置。

处理器刚启动的时候怎么知道BIOS入口在哪里呢？当然是人为强制约定，强扭的西瓜不甜，但解渴。

CPU从内存中哪个位置读取指令并执行是由PC寄存器决定的，而在开机的一瞬间，PC寄存器被强制初始化为0xFFFF0（即BIOS的入口地址），具体些，就是将段基址寄存器CS初始化为0xF000，偏移地址寄存器IP初始化为0xFFF0。

> 现代处理器在加电启动时CS寄存器依旧为0xF000，IP寄存器为0xFFF0，处理器地址线的低20位依旧为0xFFFF0。但现代处理器地址线一般远不止20根，处理器会将其余（更高位）强制为高电平，如32根地址线初始化位置就是0xFFFFFFF0. 
>
> 这样做的目的是将ROM-BIOS放到32位地址线可寻址内存范围（4GB）的最高端，使得操作系统能够得到一块连续不间断的内存，方便管理。
>
> 最终考虑到兼容性，0xFFFFFFF0和0xFFFF0都指向同一块ROM（也就是BIOS）。
>

### 本职工作

0xFFFF0-0xFFFFF一共也就16字节的空间，如果顺序执行下去自然干不了多少事，所以需要跳转到一片更广阔的地址空间。

```assembly
jmp far f000:e05b
```

前面说过启动之初所有高端地址线都被强制为高电平，直至遇到第一个段间转移指令（同时改变了段寄存器CS和指令指针寄存器IP），至此，物理地址直接取决于CS和IP。下图是bochs运行时的输出信息：

![image-20210307103651519](C:\Users\Five\Desktop\note\img\image-20210307103651519.png)

检测一些外设信息（寻找显卡）、初始化好硬件、建立中断向量表、填写中断例程。



具体代码很长，下面是前10行代码：

```assembly
xor ax ax ;应该就是ax寄存器置零的意思吧
out 0x0d, al ;从al寄存器写1字节到端口0x0d
out 0xda, al
mov al, 0xc0 ;寄存器终于不是一堆0了
out 0xd6,al 
mov al, 0x00
out 0xd4,al
mov al,0x0f
out 0x70,al ;0x70是CMOS RAM/RTC端口
in al,0x71
```

前10行代码p都看不出来，懒得再一行一行追下去了，毁灭吧，跳过吧。

### 加载主引导扇区

最后一项，加载主引导扇区。

> 加载一般是指把某I/O设备（可以是硬盘、网卡等等）上的内容（可以是程序，可以是数据，对硬件而言没有区别，都是二进制罢了）复制到内存中的过程。

重装过操作系统会知道，在启动电脑重装操作系统的时候，要在BIOS修改启动盘（硬盘、U盘、软盘、光盘等）顺序。

BIOS 会按照顺序，读取这些启动盘中位于 0 盘 0 道 1 扇区的内容。



## BIOS的发展[^2]

BIOS-MBR，BIOS-GPT，PXE（网络启动）。



### BIOS硬件的发展

BIOS最初存储在ROM中，在工厂里用特殊的方法烧录，其中的内容只能读不能改。如果发现资料有任何错误，则只有舍弃不用。

PROM（Programmable ROM）、EPROM（Erasable Programmable ROM）、EEPROM（Electrically EPROM）相继问世。

586以后的主板上BIOS ROM芯片大部分都采用EEPROM

从奔腾时代开始，现代的电脑主板都使用NORFlash来作为BIOS的存储芯片。容量比EEPROM更大、具有写入功能、写入速度快、且仅需通过软件的方式进行BIOS的更新，而无需额外的硬件支持（通常EEPROM的擦写需要不同的电压和条件）。



### UEFI：新的接口标准

#### x86和ARM

在x86的生态圈中，有Windows、Ubuntu这样的OS厂商，有Intel、AMD这样的芯片厂商，有华硕、技嘉、微星等主板厂商，更有其他各种硬件如显卡、内存的提供商。

相比较之下，Dell、联想等成品品牌机厂商（将生态圈内的东西组合后提供给用户），其技术性和话语权都相对较弱。因此x86生态体系松散且割裂。

移动端ARM体系反而不如x86这么自由，往往由品牌厂商统合整个产品，Apple自不必说，自成生态，即使是华为、小米这样的安卓机，其也往往自成生态——品牌厂商能直接对用户负责，而不是由某个硬件的提供商。

ARM社区为攻入x86优势领域也开始接受UEFI，不过不叫BIOS，而叫做Bootloader。



#### BIOS和UEFI

生态厂商的千奇百怪引出了BIOS和UEFI的最主要的功能：初始化硬件和提供硬件的软件抽象——像极了操作系统的功能。

> 某种程度上，BIOS和UEFI的确就是将操作系统的BSP部分单独封装后下放到主板或BIOS提供商完成。

> 英特尔公司从2000年开始，提出了可扩展固件接口（Unified Extensible Firmware Interface），用以规范BIOS的开发。而支持EFI规范的BIOS也被称为EFI BIOS。
>
> 之后为了推广EFI，业界多家著名公司共同成立了统一可扩展固件接口论坛（UEFI Forum），英特尔公司将EFI 1.1规范贡献给业界，用以制订新的国际标准UEFI规范。

UEFI扫除了传统BIOS割裂的生态，打通了PC固件之间的鸿沟，并提供统一的接口给操作系统。[^2]

得益于强有力的品牌商，arm系统往往可以在一开始就初始化好一些，但x86不行。x86体系的启动就像在未知的黑暗中，需要一步一步小心翼翼地摸索。[^2]



在所有平台上一致的操作系统启动服务。

UEFI和传统BIOS在启动引导过程原理上没有本质区别[^2]



下图为Hyper-V新建虚拟机时需要进行的virtual machine generation选择，其中generation2拥有UEFI-based硬件。

![image-20210306145801397](C:\Users\Five\Desktop\note\img\image-20210306145801397.png)

# 主引导扇区：0x7c00-0x7DFF

![image-20201014143101764](C:/Users/Five/Desktop/note/img/image-20201014143101764.png)

## 主引导记录和扇区

MBR，Master Boot Record，主引导记录。

主引导记录在硬盘的第一个扇区，即C/H/S地址的0柱面0磁头1扇区，也即主引导扇区。主引导扇区是开机后访问硬盘所必须要读取的第一个扇区。

* 也将其开头的446字节内容特指为“主引导记录”（MBR）
  * 检查分区表正确性。
  * 加载并跳转到磁盘上的引导程序。
* 446字节后是4个16字节的“磁盘分区表”（DPT）[^5]
  * 所以一个硬盘最多只能分四个一级分区
  * 每个分区的16个字节具体内容对应如下
    * 第1个字节：如果为0x80，就表示该主分区是激活分区，控制权要转交给这个分区。
      * 四个主分区里面只能有一个是激活的。
      * 计算机会读取激活分区的第一个扇区VBR，Volume boot record
    * 第2-4个字节：主分区第一个扇区的物理位置（柱面、磁头、扇区号等等）。
    * 第5个字节：主分区类型。
    * 第6-8个字节：主分区最后一个扇区的物理位置。
    * 第9-12字节：该主分区第一个扇区的逻辑地址。
    * 第13-16字节：主分区的扇区总数。
      * 4个字节意味着单个分区最多$2^{32}$个扇区，扇区逻辑地址也是32位
      * 每个扇区512KB记，单个分区最多2TB
* 最后是2字节的结束标志（0x55AA）
  * 如果没有55AA的结束标志，BIOS会顺序读取下一个设备的主引导扇区，查看是否符合条件。
* 共512字节，一个完整扇区。

如下所示的汇编代码在经过汇编后再写入磁盘后就是一份合法的主引导记录——当然它起不到加载操作系统的功能，只能在显示屏界面上显示`Hello World!`，并且会陷入死循环（避免执行到非法内存，死循环是权宜之计）。

```assembly
mov dx,0xb800
mov es,dx

mov byte [es:0x00],'H'
mov byte [es:0x01],0x0F
mov byte [es:0x02],'e'
mov byte [es:0x03],0x0F
mov byte [es:0x04],'l'
mov byte [es:0x05],0x0F
mov byte [es:0x06],'l'
mov byte [es:0x07],0x0F
mov byte [es:0x08],'o'
mov byte [es:0x09],0x0F
mov byte [es:0x0A],','
mov byte [es:0x0B],0x0F
mov byte [es:0x0C],'w'
mov byte [es:0x0D],0x0F
mov byte [es:0x0E],'o'
mov byte [es:0x0F],0x0F
mov byte [es:0x10],'r'
mov byte [es:0x11],0x0F
mov byte [es:0x12],'l'
mov byte [es:0x13],0x0F
mov byte [es:0x14],'d'
mov byte [es:0x15],0x0F
mov byte [es:0x16],'!'
mov byte [es:0x17],0x0F

infi: jmp near infi

times 358 db 0

dw 0xaa55
```





```assembly
; hello-os
; TAB=4

  ORG  0x7c00   ;程序加载到内存的 0x7c00 这个位置

;程序主体

entry:
  MOV  AX,0   ;初始化寄存器
  MOV  SS,AX
  MOV  SP,0x7c00
  MOV  DS,AX   ;段寄存器初始化为 0
  MOV  ES,AX
  MOV  SI,msg
putloop:
  MOV  AL,[SI]
  ADD  SI,1
  CMP  AL,0   ;如果遇到 0 结尾的，就跳出循环不再打印新字符
  JE  fin
  MOV  AH,0x0e   ;指定文字
  MOV  BX,15   ;指定颜色
  INT  0x10   ;调用 BIOS 显示字符函数
  JMP  putloop
fin:
  HLT
  JMP  fin
msg:
  DB  0x0a,0x0a  ;换行、换行
  DB  "hello-os"
  DB  0x0a   ;换行
  DB  0    ;0 结尾

  RESB 0x7dfe-$   ;填充0到512字节
  DB 0x55, 0xaa   ;可启动设备标识
```



> 为什么需要先读取主引导记录，而不直接读取操作系统？

1. 磁盘是有文件系统的，NTFS、FAT等等，不同的机器可能会有不同的文件系统，还有各种分区信息
2. 于是增加约定，使不同的文件系统都能用同样的方式读到第一块——引导扇区
3. 用引导扇区识别分区等信息，然后读取操作系统内核



### Why 0x7c00[^1]

将主引导扇区的内容复制到0x7c00后，CPU会跳转至此（PC寄存器变为0x7c00）。

但为什么是0x7c00到这么个奇奇怪怪、比4KB小128B（或者说比32Kb小1024bit）的地址？也不凑个整啥的？

> 1981年8月发布的IBM 5150是很多x86 PC的祖先，IBM 5150配置Intel 8086和（最低配置）16KB的内存。当时搭配的操作系统是86-DOS，这个操作系统内存最少需要32KB（16KB的最低配置直接不配拥有86-DOS）。
>
> `0x7c00`在该电脑的BIOS上首次出现，并一路作为规范被继承了下来。

BIOS developer team decided 0x7C00 because:

1. They wanted to leave as much room as possible for the OS to load itself within the 32KiB.
2. 8086/8088 used 0x0 - 0x3FF for interrupts vector, and BIOS data area was after it.
3. The boot sector was 512 bytes, and stack/data area for boot program needed more 512 bytes.
4. So, 0x7C00, the last 1024B of 32KiB was chosen.

即：

8088芯片本身需要占用`0x0000～0x03FF`，用来保存各种中断处理程序的储存位置。所以，内存只剩下`0x0400～0x7FFF`可以使用。

为了把尽量多的连续内存留给操作系统，主引导记录就被放到了内存地址的尾部。由于一个扇区是512字节，主引导记录本身也会产生数据，再留出512字节，一共1KB。

所以32KB末尾的1KB留给了主引导记录，也即其预留位置为0x7FFF - 512 - 512 + 1 = 0x7C00 。



至此，32KB的内存分配如下表所示。

| 地址          | 作用               |
| ------------- | ------------------ |
| 0x0-0x400     | Interrupts Vectors |
| 0x400-0x5??   | BIOS data area     |
| 0x5??-0x7c00  | OS load area       |
| 0x7c00-0x7E00 | Boot Sector        |
| 0x7E00-0x7FFF | Boot data/stack    |



### 扩展分区







## 分区引导扇区

从主引导扇区跳转到特定的分区引导扇区。扇区结构：

![image-20201014154158223](C:/Users/Five/Desktop/note/img/image-20201014154158223.png)

* 跳转指令JMP
  * 平台相关，不同指令集JMP指令不同
* 文件卷头结构
  * 文件系统描述信息
* 启动代码

后跟2字节结束标志55AA。



## 加载并执行加载程序

![image-20201014154700059](C:/Users/Five/Desktop/note/img/image-20201014154700059.png)



1. 将加载程序从磁盘的引导扇区（512字节）加载到0x7c00
2. 跳转到CS:IP=0000:7c00
3. 运行加载程序

将操作系统的代码和数据从硬盘加载到内存中，并跳转到操作系统的起始地址。

最后开始执行操作系统程序









[^1]:Why BIOS loads MBR into 0x7C00 in x86  https://www.glamenv-septzen.net/en/view/6
[^2]:UEFI 引导与 BIOS 引导在原理上有什么区别？ - 老狼的回答 - 知乎 https://www.zhihu.com/question/21672895/answer/774538058
[^3]:全网最硬核讲解计算机的启动过程 - 闪客sun的文章 - 知乎 https://zhuanlan.zhihu.com/p/113536449
[^4]:《x86汇编：从实模式到保护模式》
[^5]:http://www.ruanyifeng.com/blog/2013/02/booting.html
[^6]:计算机是如何启动的 https://www.dingmos.com/2019/12/15/%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%98%AF%E5%A6%82%E4%BD%95%E5%90%AF%E5%8A%A8%E7%9A%84.html
[^7]:https://www.dingmos.com/