> 为什么要建模？因为代码不够直观，全局性很差。

# UML

> 1994年10月，Grady Booch和Jim Rumbaugh首先将Booch 93和OMT-2统一起来，并于1995年10月发布了UM 0.8。
>
> 1996年6月和10月，发布了UML 0.9和UML 0.91两个版本（UM重命名为UML）。
>
> 1997年正式公布UML 1.0，随后OMG（Object Management Group）接纳UML 1.1作为基于面向对象技术的标准建模语言。
>
> 2004年1月，UML 1.4.2被国际标准化组织吸收为国际标准，编号ISO/IEC 19501。
>
> 截至目前最新版为2017年，UML 2.5.1，[官网](https://www.omg.org/spec/UML/)可以下载UML的参考文档



## 元素：顶点和边

UML定义了两类模型元素：

* 一类用于表示模型中的某个概念，如类、对象、构建、用力、结点、接口、包、注释等，我将他们视为图的顶点（or集合元素）。
* 一类用于表示模型元素之间项目连接的关系，主要又关联、泛化、依赖、实现、聚集和组合等，我将他们视为图的边（or关系）。

![image-20210111215654786](C:\Users\Five\Desktop\note\img\image-20210111215654786.png)



![image-20210111215748714](C:\Users\Five\Desktop\note\img\image-20210111215748714.png)

### 元模型结构

UML模型可定义为四个抽象层次：用户模型、模型、元模型、元元模型（好家伙，隔这套娃呢）。

元模型定义了用于描述模型的语言。

模型是对现实世界的抽象，无论是问题领域还是解决方案，都可以抽象成模型。

用户模型是模型的示例，用于表达一个模型的特定情况。



元元模型和元模型之间、元模型和模型之间、模型和用户模型之间的关系都类似于类和示例的关系。



## 建模和图

静态图有用例图、类图、对象图、构件图、部署图。

动态图有状态图、时序图、协作图、活动图。

> 静态建模（静态图）是对模型在空间维度上的描述，动态建模（动态图）是对模型在时间维度上变化的描述。

### 静态建模

* 用例图
* 类图
* 对象图





### 动态建模

* 状态图
* 时序图
* 协作图
* 活动图





### 视图

用例视图、逻辑视图、进程视图、构建视图、部署视图。

每个视图由一组图构成。





## 指点江山时间

也许我不配对UML指指点点，但Who care呢。

UML好吗？能被推为规范的一定不会差到哪里去。

但我们指的需要UML吗？未必。UML太细了

* 我们总是要在简洁和完整之间做取舍，从一个工科的角度而言，UML显然有些“病态”地追求后者
* 绝大部分，甚至私以为99%以上的项目不会需要这么详细的UML
  * 都说好的UML能直接生成代码
  * 但这么细致的UML，对于需求变动稍稍频繁一丢丢的项目，就不合适了。
  * 更改代码已经很累了，在更改UML，双倍工作量，谁受得了

也许我们需要一个简介些的模型，比如C4 Model。



# C4 model[^3]

## 概述

C4指System Context、Container、Component、Code这四个层级结构。

4也可以理解为泛指，你的软件很小时，当然可以抽掉System Context变成C3，你的应用很大，当然可以视Context为子系统，构建的更大的架构图。

![image-20210109220816567](C:\Users\Five\Desktop\note\img\image-20210109220816567.png)



架构图应该像地图软件一样，在不同尺度提供不同程度细致的信息：

![image-20210109221108832](C:\Users\Five\Desktop\note\img\image-20210109221108832.png)



* System Context Level

![image-20210109221643972](C:\Users\Five\Desktop\note\img\image-20210109221643972.png)



* Container Level

![image-20210109221924709](C:\Users\Five\Desktop\note\img\image-20210109221924709.png)



* Component Level

![image-20210109222227438](C:\Users\Five\Desktop\note\img\image-20210109222227438.png)





* Code Level

> **Don't Recommend to draw Code Level Diagram!**

![image-20210109222357962](C:\Users\Five\Desktop\note\img\image-20210109222357962.png)



## Notation

* Beware of hiding the true story
* Add more words to make the intent explicit

![image-20210109223218167](C:\Users\Five\Desktop\note\img\image-20210109223218167.png)

![](C:\Users\Five\Desktop\note\img\image-20210109223305154.png)



### General

* Does the diagram have a title? 
* Do you understand what the diagram type is?
* Do you understand what the diagram scope is?
* Does the diagram have a key/legend?



### Elements

* Does every elements have a name?
* Do you understand the type of every element? (i.e. the level of abstraction; e.g. software system, container, etc)
* Do you understand what every element does?
* Where applicable, do you understand the technology choices associated with every element?
* Do you understand the meaning of all border styles used? (e.g. solid, dashed, etc)



### Relationships

* Does every line have a label describing the intent of that relationship?
* Where applicable, do you understand the technology choices associated with every relationship? (e.g. protocols for inter-process communication)
* Do you understand the meaning of all acronyms and abbreviations used?
* Do you understand the meaning of all colours used?
* Do you understand the meaning of all line styles used? (e.g. solid, dashed, etc)



## FAQ

> Q: Isn't the C4 model a step backwards? Why are you reinventing UML? Why not just use UML?
>
> A: Whether you see the C4 model as a step forwards or a step backwards depends upon where you are. If you're using UML (or SysML, ArchiMate, etc) and it's working for you, stick with it. Unfortunately, UML usage seems to be in decline, and many teams have reverted to using ad hoc boxes and lines diagrams once again. Given that many of those teams don't want to use UML (for various reasons), the C4 model helps introduce some structure and discipline into the way software architecture is communicated. For many teams, the C4 model is sufficient. And for others, perhaps it's a stepping stone to UML.



> Q: What's the inspiration behind the C4 model?
>
> A: The C4 model was inspired by the [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) and the [4+1 model for software architecture](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model). In summary, you can think of the C4 model as a simplified version of the underlying concepts, designed to (1) make it easier for software developers to describe and understand how a software system works and (2) to minimise the gap between the software architecture model/description and the source code.
>
> The roots of the C4 model, and the various diagram types within it, can be traced back to somewhere in the region of 2006, although the "C4" name came much later, around the end of 2011. It was created during a time where teams, influenced by the agile movement, were less than enthusiastic about using UML.



> Q: Can we change the terminology?
>
> A: This terminology (context, containers, components and code) works for many organisations and many types of software. However, sometimes an organisation will have an existing terminology that people are already familiar with. Or perhaps "components" and "classes" don't easily map on to the technology being used (e.g. functional languages often use the terms "module" and "function").
>
> Feel free to modify the terminology that you use to describe software architecture at different levels of abstraction. Just make sure that everybody explicitly understands it.





## C4-PlantUML

```plantuml
@startuml C4_Elements
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```



# MS Visio

MS还是你MS。兜兜转转，找各种画UML的工具，最后才想起来Visio，真香。





# Rational Software

> Rational Machines was founded by Paul Levy and Mike Devlin in 1981 to provide tools to expand the use of modern software engineering practices, particularly explicit modular architecture and iterative development.
>
> It changed its name in 1994 to Rational Software, and was sold for US\$2.1 billion to IBM on February 20, 2003.[^1]



## Rational Rose XDE

Rational Rose XDE, an "eXtended Development Environment" for software developers, integrates with MSVS .NET and Rational Application Developer.[^2]



Rational Rose系列资料又少，还贵的离谱，我会受这鸟气？弃之，寻开源。



# UMLet





# Archi

What does ArchiMate provide?

* A language with concepts to describe architectures
* A framework to organize these concepts
* A graphical notation for these concepts
* A vision on visualizations for different stakeholders
* An open standard maintained by The Open Group



# Plant UML













[^1]: Wikipedia Rational Software https://en.wikipedia.org/wiki/Rational_Software
[^2]: Wikipedia Rational XDE https://en.wikipedia.org/wiki/IBM_Rational_Rose_XDE
[^3]:c4model官网 https://c4model.com/  infoQ上有中文译文。