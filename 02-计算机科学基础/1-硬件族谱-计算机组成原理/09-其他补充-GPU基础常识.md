> 天下GPU共一石，NVIDIA独得八斗，AMD得一斗，其余厂商共分一斗。
>
> （但实际上没有另一个上得了台面的独显厂商了，这一斗也是NVIDIA和AMD的）
>
> （尽管Intel有更胜NVIDIA和AMD的GPU出货量，但基本是配套销售，即不太用于高性能计算等领域）

# GPU相关概念

## 显卡和GPU

GPU和显卡常混为一谈，但严格来说并不是同一个东西。GPU是Nvidia提出的概念，是显卡上的一块芯片。就像CPU是主板上的一块芯片。

![](C:/Users/Five/Desktop/note/img/19b63db9de101fb471d7eb010c2ede86_1440w.jpg)

原始的显卡一般都是集成在主板上，只完成最基本的信号输出工作，并不用来处理数据。随着显卡的迅速发展，就出现了GPU的概念，显卡也分为独立显卡和集成显卡。

## 显卡驱动

通常指NVIDIA Driver。





## 主流GPU架构和型号（NVIDIA为主）

![](C:/Users/Five/Desktop/note/img/20210302203003663.png)



NVIDAI型号：

* Tegra：手机和嵌入式设备
* GeForce：主要用于电脑显卡，也是最具知名度的
  * 从2004年的Geforce 6800系列开始就有“GT”的代号，Graphics Processor protoType，是加强版的意思，如8600GT是8600的加强版。
  * 到了2005年的7800系列，引入了“GTX”的代号，即GT eXtreme，直接代表着高端或者顶级显卡。
  * 关于系列
    * 2008年，NVIDIA的新一代使用GT200的显卡GTX260/GTX280发布。（即200系）
    * 2010年，NVIDIA发布GTX480/470（即400系）
    * 2012年，NVIDIA发布代号Kepler的GTX680（即600系）
    * ……后续900系列等
    * 2016年，NVIDIA 正式发布了新一代旗舰显卡 Geforce GTX 1080
  * 2000系列，出现了“RTX”，这里的“RT”就代表着光线追踪（ray tracing的缩写）（GTX基础上的另一次增强）
* Quadro：专业绘图
* Tesla：大规模计算，



| 架构     | Tesla                  | Fermi | Kepler | Maxwell | Pascal                         | Volta                | Turing | Ampere |
| -------- | ---------------------- | ----- | ------ | ------- | ------------------------------ | -------------------- | ------ | ------ |
| 大致时间 | 2008                   | 2010  | 2012   | 2014    | 2016                           | 2017                 | 2018   | 2020   |
| 相应产品 | 市面上很难找到相应显卡 |       |        |         | Tesla P100，GTX 1080/1070/1060 | Tesla V100，GTX 1180 |        |        |
|          |                        |       |        |         |                                |                      |        |        |







## GPU简史

GPU历史系列（三）：Nvidia一统江湖 - 张竞扬 摩尔精英的文章 - 知乎 https://zhuanlan.zhihu.com/p/138675217

以后有机会再填坑——大概率没有。



# CUDA相关概念

Compute Unified Device Architecture，NVIDIA推出的运算平台。

有人说CUDA就是一门编程语言，像C,C++,python 一样，有人说CUDA是API ，也有人（包括官方）说CUDA是平台 —— 总之，通过CUDA能便捷且有效（同时简单且优雅）地调用GPU资源完成计算任务。



[[CUDA_Toolkit_Release_Notes.pdf]]

## Toolkit

主要核心组件包括

* Complier：编译器
* Tools
* Libraires
* Samples：各种演示示例
* CUDA Driveres：

## Libraries and Middleware	

### cuDNN

专为深度学习计算设计的软件库。







## 基本命令

```
nvidia-smi
```

smi 的全称是System Management Interface。



# OpenCL

