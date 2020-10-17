# 实验概述

## 基本实验环境

* Ubuntu
* shell命令
* 系统维护工具
* 源码阅读与编辑工具
* 源码比较工具：diff，meld
* 开发编译调试工具：gcc，gdb，make
* 硬件模拟器：qemu

### 基于Windows自带Hyper-V搭建环境

个人偏好，Windows原生Hyper-V。

1. 下载课程给出的[实验虚拟硬盘-VHI文件](https://pan.baidu.com/s/11zjRK)

2. （还是要用到VirtualBox）用VirtualBox自带的工具转换VHI到Hyper-V可用的VHD文件

   ```
   VBoxManage.exe clonehd mooc-os-2015.vdi mooc-os-2015.vhd -format VHD
   ```

3. 然后就跟课程用VirtualBox一样用Hyper-V即可



## 先验知识

### X86-32硬件知识

#### 80386运行模式

##### 实模式

80386加点启动后处于实模式运行状态，可访问的物理内存空间不超过1MB，且无法发挥Intel80386以上级别的32位CPU的4GB内存管理能力。

##### 保护模式

支持内存分页模式，提供对虚拟内存的良好支持。

支持优先级机制，不同程序可以运行在不同的优先级上。操作系统运行在最高的优先级0上。

##### SMM模式

#### 80386内存架构

##### 物理内存地址空间

就内存条上真实存在的物理存储。


##### 线性地址空间

操作系统的虚拟管理下，每个应用程序能够访问的地址空间。

每个运行的应用程序都认为自己独享整个计算机系统的地址空间。


##### 逻辑地址空间

应用程序直接使用的地址空间。



##### 寻址过程

段机制启动、页机制未启动：

```mermaid
graph LR
A[逻辑地址]-->|段处理机制| C[线性地址=物理地址]
```

段、页机制都启动：

```mermaid
graph LR
A[逻辑地址]-->|段处理机制| C
C[线性地址]-->|页处理机制| E
E[物理地址]
```



#### 80386寄存器

##### 通用寄存器

* EAX，累加器
* EBX，基址寄存器
* ECX，计数器
* EDX，数据寄存器
* ESI，源地址指针寄存器
* EDI，目的地址指针寄存器
* EBP，基址指针寄存器
* ESP，堆栈指针寄存器



##### 段寄存器

* CS，Code Segment，代码段
* DS，Data Segment，数据段
* ES，Extra Segment，附加数据段
* SS，Stack Segment，堆栈段
* FS，附加段
* GS，附加段



##### 指令指针、标志寄存器

EIP，指令寄存器

EFLAGS，标志寄存器



##### 其他寄存器

控制寄存器

系统地址寄存器

调试寄存器

测试寄存器



### ucore编程方法和通用数据结构

* 面向对象、面向过程等编程方法
* 数据结构和算法基础知识





# 启动、中断和系统调用

## x86启动顺序

### 从BIOS到Bootloader

x86寄存器初始值：

![image-20201016083943958](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016083943958.png)

其中CS:EIP（CS<<4+EIP）决定了从哪个地址开始取得相应的指令去执行。

即第一个实际地址是$Base + EIP = FFFF0000H + 0000FFF0H = FFFFFFF0H$，这是BIOS的EPROM（Erasable Programmable Read Only Memory）所在地。

![image-20201016084657613](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201016084657613.png)

所以其实段寄存器在表示地址时的最小单位是$2^4=16$字节。而一个段最大长度也就是Offset的最大值$2^{16}=64KB$

> 此时还没有进入保护模式，没有段机制、页机制，二十位总线也只能访问1MB内存

跳转到BIOS的EPROM所在地后开始运行BIOS并加载主引导扇区。

1. BIOS加载存储设备上的第一个扇区（512字节）的内容到内存的0x7c00
2. 跳转到0x7c00开始执行bootloader



### 从Bootloader到OS

#### Enable保护模式

Enbale段机制，从实模式的20位（1M）寻址空间，切换到了32位（4G）的寻址空间。

#### 读取kernel

读取ELF文件格式的Kernel（往往在主引导扇区后），并存放到内存中的固定地点

#### 控制权移交OS

从Bootloader跳转到OS的入口点开始执行。



### 段机制

