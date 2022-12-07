![image-20201014143744361](C:/Users/Five/Desktop/note/img/image-20201014143744361.png)

uCore，清华大学教学实验操作系统

![](C:/Users/Five/Desktop/note/img/image001.png)



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



# 实验1：bootloader

## x86启动顺序

### 从BIOS到Bootloader

x86寄存器初始值：

![image-20201016083943958](C:/Users/Five/Desktop/note/img/image-20201016083943958.png)

其中CS:EIP（CS<<4+EIP）决定了从哪个地址开始取得相应的指令去执行。

即第一个实际地址是$Base + EIP = FFFF0000H + 0000FFF0H = FFFFFFF0H$，这是BIOS的EPROM（Erasable Programmable Read Only Memory）所在地。

![image-20201016084657613](C:/Users/Five/Desktop/note/img/image-20201016084657613.png)

所以其实段寄存器在表示地址时的最小粒度是$2^4=16$字节。而一个段最大长度也就是Offset的最大值$2^{16}=64KB$

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







# 实验2：内存管理







# 实验3：内核线程管理



# 实验4：用户进程管理





# 实验5：处理器调度





# 实验6：文件系统

