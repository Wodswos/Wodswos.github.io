OpenHarmony和手机端的Harmony OS并不是同一个东西，前者是LliteOS内核，公开全量源代码。



> OpenHarmony 1.0应该是鸿蒙项目的初衷（物联网系统），用C语言很正常。liteos 确实是实时内核，但这种低功耗轻量kernel方案[^2]移植不到手机的 Harmony OS 2.0 上。后者至今仍是闭源，从第一批OTA升级用户的反馈看，用的似乎是Linux 4.14 kernel。[^1]



# LiteOS

Huawei LiteOS 是华为**面向IoT领域**，构建的**轻量级**物联网操作系统，遵循BSD-3开源许可协议。

可广泛应用于智能家居、个人穿戴、车联网、城市公共服务、制造业等领域。大幅降低设备布置及维护成本，有效降低开发门槛、缩短开发周期。

LiteOS Kernel是Huawei LiteOS 操作系统基础内核，包括任务管理、内存管理、时间管理、通信机制、中断管理、队列管理、事件管理、定时器等操作系统基础组件，可以单独运行。

- 高实时性，高稳定性
- 超小内核，基础内核体积可以裁剪至不到10K
- 低功耗
- 支持功能静态裁剪

> 而鸿蒙是基于微内核的全场景分布式OS，某种程度上的LiteOS+++++++++版本。

## 吹水环节

* 分布式架构首次用于终端OS，实现跨终端无缝协同体验
* 确定时延引擎和高性能IPC技术实现系统天生流畅
* 基于微内核架构重塑终端设备可信安全
* 通过统一IDE支撑一次开发，多端部署，实现跨终端生态共享



## LiteOS Studio







# Harmony OS，又称PPT OS

![v2-b6528361959a280fb02142427a6ad5e5_r](C:\Users\Five\Desktop\note\img\v2-b6528361959a280fb02142427a6ad5e5_r.jpg)







[^1]:如何看待鸿蒙os里全是android痕迹? - 贾靳的回答 - 知乎 https://www.zhihu.com/question/339790377/answer/1638216618
[^2]:https://github.com/LiteOS/LiteOS

