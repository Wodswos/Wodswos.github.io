# 一些基本概念

lib、package、module、project、jar、war，尼玛概念是真的多，乱是真的乱。

## Project、Module、Package

### project和module

缺省情况下，IDEA默认单Project单Module，此时Project和Module是一对一的关系。

但一个Project可以有多个Module。

### 不同视角下的项目结构

IDEA中可以选择项目结构的视角，也许可以借此理解一个project的结构到底是怎样的

#### package vs Project

package视角下应该就是比较纯粹的java代码的目录结构信息

project视角下会有更多的信息



下图是Android Studio（IDEA改）中一个Android项目的结构示例：

![image-20210102215211236](C:\Users\Five\Desktop\note\img\image-20210102215211236.png)





### package=文件夹？module=文件夹？





### Web工程源代码和编译结果比较

![image-20210103164253197](C:\Users\Five\Desktop\note\img\image-20210103164253197.png)

## 打包：jar和war[^6]

JAR，Java Archive，即以zip压缩方式归档文件。

 JAR 中包含特殊的文件，如 manifests 和部署描述符，用来指示工具如何处理特定的 JAR。



* war包是Sun提出的一种web应用程序格式，与jar类似，是很多文件的压缩包。
* war包中的文件按照一定目录结构来组织。
  * 根目录下包含有html和jsp文件，或者包含有这两种文件的目录，以及WEB-INF目录
  * WEB-INF目录包含web.xml文件和一个classes目录
    * web.xml是这个应用的配置文件
    * classes目录下则包含编译好的servlet类和jsp，或者servlet所依赖的其他类（如JavaBean）。
    * 通常这些所依赖的类也可以打包成jar包放在WEB-INF下的lib目录下。







# IDEA

应该算是最主流的Java开发IDE了吧。

## Project Structure

Project Settings有Project、Module、Libraries、Facets、Artifacts一堆东西



# Maven

![](C:/Users/Five/Desktop/note/img/v2-b8463b0298caa3625236ef0cbb1a6291_1440w.jpg)

Android项目只能用Gradle，在Java后端领域，Maven依旧占优。[^1]

* Gradle不比Maven好
* Maven也不比Gradle好

优点

* 通过统一的流程完成工作
* 社区很大，插件很多很丰富

缺点

* 过分死板
  * 很多仓库通过脚本，用exec插件完成更灵活的工作
* 新功能少，更新保守
* 对于大项目全量构建代价大

## 起源、诉求

当我们作为一个新手开发JavaWeb的时候，往往会遇到很多问题

* 一个项目就是一个工程，大项目会变得很臃肿



如果一个项目非常庞大，就不再适合继续使用package的概念来进行简单的模块划分。

> 没有什么复杂的项目是添加一个抽象层不能解决的，如果有，就加两个。——尼古拉·吴

所以需要在package和project中间增加一个module的概念，起到对项目合理的分工作用。

而借助Maven，可以实现将一个Project拆分成多个Module。



* 项目中用到的Jar包需要手动复制粘贴或导入到WEB-INF/lib目录下

* Jar包依赖的其他Jar包也需要自己手动导入，依赖层层递进，需要自己追踪、管理依赖关系
  * 如commons-fileupload-1.3.jar需要依赖commons-io-2.0.1.jar
  * 随着项目架构变大，依赖关系加深，极大增加程序员学习成本和负担
* Jar包需要从各式各样的渠道获取，很麻烦
  * 渠道本身也很难找到（在没有Maven的时候）



借助Maven，可以将需要用到的Jar包统一保存在仓库（中央仓库）中，当工程需要该Jar包时，直接可以到仓库访问该Jar包。



> 运行时环境：如JRE（Java Runtime Enviroment）、Tomcat等。
>
> 在IDE中开发时，往往需要引用运行时环境，但不需要真的把运行时环境相关的所有Jar包复制到项目中。
>
> 这种引用有点类似Maven从仓库中引用Jar包，但Maven在导出项目时可以选择将Jar包真正放入项目中。



## Maven基础知识

### Maven是什么

* Maven是一款主要服务于Java的自动化构建工具
  * Make→Ant→Maven→Gradle
  * 构建：以Java源文件、框架配置文件、HTML、多媒体资源等Resouce为原材料去生产一个可运行项目的过程
  * 构建通常包含的过程
    * 清理：删除旧的Class字节码文件
    * 编译：将Java源程序编译为class字节码文件
    * 测试、报告：自动测试，调用JUnit，返回测试程序执行结果
    * 打包：动态Web工程打war包，Java工程打Jar包（zip）
    * 安装：Maven特定的概念，将打包后的文件复制（或者说备份/更新）到“仓库”
    * 部署：将war包等部署到Servlet容器等，使其可运行。

> Maven产生的年代IDE还没有那么普及，现如今很多IDE（Eclipse、IntelliJ）在很多时候已经帮用户做好了这些工作。
>
> （当然我并不觉得IDE和Maven是替代的关系，Maven更多的是一种工程范式，IDE是辅助工具，后者算是前者的一种实现）
>
> 就像C++的使用者，用GCC、Make（等工具栈）和Visual Studio（IDE）完全是不同的世界。



JavaWeb工程源代码和编译（构建）结果比较：

![image-20210103164253197](C:\Users\Five\Desktop\note\img\image-20210103164253197.png)



### Maven Get Started

配置Maven啥的就不赘述了。

![image-20210103172039661](C:\Users\Five\Desktop\note\img\image-20210103172039661.png)

使用Maven需要按照约定创建目录结构。

>  Maven负责项目的自动化构建，自然需要知道待处理文件位置等信息，即Maven要了解项目结构。框架和用户交流可以有如下两种方法：
>
> * 以配置的方式告诉框架
> * 由框架告诉用户该遵守的约定
>
> 各种`xml`文件就是通过第一种方式。

> 默认的规矩：约定 > 配置 > 编码，这种规矩也从某种程度上隐含着编程水平的积累和提升方向。
>
> *	最开始用编码去解决问题是很简单的，但代码很死，功能也很单一；
> *	当开始用“配置”去解决问题的时候，考验的是对整个项目/业务是否有框架性的理解；
> *	而当试着用“约定”去解决问题时，考验的是对整个技术栈的认知和理解。





### pom.xml

Maven配置的核心文件。



# Gradle

![image-20210103191229454](C:\Users\Five\Desktop\note\img\image-20210103191229454.png)

Gradle是一个基于Apache Ant和Apache Maven概念的项目自动化建构工具。它使用一种基于Groovy的特定领域语言来声明项目设置，而不是传统的XML。当前其支持的语言限于Java、Groovy和Scala，计划未来将支持更多的语言。

> 2020年6月，Spring Boot团队宣布将他们的build迁移到了Gradle。[^1]

优点

* 足够自由、足够灵活

缺点

* 臃肿庞大，概念复杂繁多，学习曲线陡峭
* 变化太快，社区跟不上

> 其实Gradle的新功能都不是空穴来风，我们有些重要客户在内部广泛使用Gradle，会定期和我们反馈问题和需求。脚步太快造成社区措手不及，新功能只有那么几家会使用。[^1]



## Gradle概览

项目结构与Maven类似（或者说大部分Java Application都类似）

![image-20210103133627396](C:\Users\Five\Desktop\note\img\image-20210103133627396.png)

在`bin`目录下有用于Windows环境的`.bat`命令和用于Linux/MacOS环境的Shell脚本。

* Gradle是一个通用的自动化构建工具，而不针对某个特定平台及语言
* 核心模式是基于Task的
  * Task是Gradle的最小执行单元，由输入、动作、输出三部分构成
  * 前一个Task的输出是后一个Task的输入



> 构建脚本基于API调用，而非基于配置 你可以将构建脚本当代码阅读，而不是配置文件。它只会告诉你如何一步一步的将软件构建出来，而不会告诉你每一步是如何做的。这也是与我们日常工作最密切的部分。



### 语法元素

* `Project`

build script的隐含对象，通过它来使用gradle的功能。

* 属性

能使用`=`和`$` (模板符号)的都是属性

```groovy
version = '1.0.1' myCopyTask.description = 'Copies some files'
 file("$buildDir/classes") println "Destination: ${myCopyTask.destinationDir}" 
```

* 方法



* Block

一种特殊的方法。



### lifecycle

* Initialization
* Configuration
* Execution



### 自定义扩展

* 自定义Task类型
* 自定义Task动作，如`doFirst()`、`doLast()`等方法



## Gradle基础使用

编写`build.gradle`文件

```groovy
 task hello{       
     doLast{ println "hello world!" }  
 }
```

task是gradle的Api, 其是Project 接口的一个方法，签名如下

```java
//Creates a {@link Task} with the given name and adds it to this project.
Task task(String name) throws InvalidUserDataException;
```

在命令行运行gradle

```shell
# hello是task名
gradle hello
```



### Task依赖

```groovy
task hello {
    doLast {
        println 'Hello world!'
    }
}
task intro {
    dependsOn hello
    doLast {
        println "I'm Gradle"
    }
}
```





```shell
gradlew --stop
```

杀死相同版本的所有Deamon



## Gradle Wrapper

> - Gradle是个构建系统，能够简化你的编译、打包、测试过程。熟悉Java的同学，可以把Gradle类比成Maven。
> - Gradle Wrapper的作用是简化Gradle本身的安装、部署。不同版本的项目可能需要不同版本的Gradle，手工部署的话比较麻烦，而且可能产生冲突，所以需要Gradle Wrapper帮你搞定这些事情。Gradle Wrapper是Gradle项目的一部分。
> - Android Plugin for Gradle是一堆适合Android开发的Gradle插件的集合，主要由Google的Android团队开发，Gradle不是Android的专属构建系统，但是有了Android Plugin for Gradle的话，你会发现使用Gradle构建Android项目尤其的简单。[^5]







```shell
gradlew compileJava
```

1. 会首先启动一个非常轻量的JVM去检查当前机器是否有安装对应版本的Gradle，没有则下载安装。
2. 查找对应版本的daemon JVM，若没有找到，则启动一个，否则直接连接该Daemon JVM

运行如下命令

```bash
gradle wrapper
```

会生成文件夹`gradle`，以及`gradlew`和`gradlew.bat`对应两个不同系统的脚本。

在文件夹`gradle`中有`gradle-wrapper.jar`和`gradle-wrapper.properties`两个文件。jar包的用处是下载真正的Distribution。

```bash
gradlew wrapper
```







## Daemon

当构建的时候，Gradle会启动一个Client的JVM，用于和Daemon JVM通信。

当你构建结束后，Client JVM会销毁，但Deamon JVM不会销毁。当需要新一轮的构建时，只需要创建一个Client JVM，其开销会变小很多，而且很多上一次也用到的Jar包能够得到缓存。

> 新的Client JVM可能会和原来的Daemon JVM不适配，此时会启动一个新的Daemon JVM
>
> 缺省下，Daemon空闲三个小时会自动退出。

使用`--no-daemon`参数可以即用即销毁（像Maven一样）。





## 用Gradle开发不同特性的APK







> gradle是构建工具，为了构建，带有依赖缓存功能（不是包管理功能）
>
> maven是依赖包管理工具，通过插件带有一定的构建能力。
>
> 看清楚他们的侧重点没有，gradle可以完成非常复杂的构建，你用它的dsl可以玩出各种花样来，所以它特别适合android这种重客户端，组件越多越复杂的应用（本质就是巨石应用）它越得心应手，反之如果你没有特别复杂的打包要求，那你就是在用牛刀杀鸡了。[^2]





# Ant





[^1]:Gradle 比 Maven 好为什么用的人少？ - blindpirate的回答 - 知乎 https://www.zhihu.com/question/276078446/answer/649632118
[^2]:Gradle 比 Maven 好为什么用的人少？ - 有铭的回答 - 知乎 https://www.zhihu.com/question/276078446/answer/968291387
[^3]:bilibili尚硅谷Maven视频 https://www.bilibili.com/video/BV1TW411g7hP
[^4]:秒懂Gradle之从完全懵逼到是懂非懂 - shusheng007的文章 - 知乎 https://zhuanlan.zhihu.com/p/148172832
[^5]:https://www.cnblogs.com/jiangxinnju/p/8229129.html
[^6]:Java程序员的日常 https://www.jianshu.com/p/3b5c45e8e5bd