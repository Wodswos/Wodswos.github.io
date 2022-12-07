> 参考书：
>
> 《Getting Started with Storm》
>
> 《Storm Real-time Processing Cookbook》PACKT出版社
>
> 《Storm Blueprints: Patterns for Distributed Real-time Computation》PACKT出版社
>
> 《Learning Storm》PACKT出版社
>
> PACKT Publishing是世界上发展最快和产品最丰富的技术书籍出版商之一。PACKT Publishing公司的书籍关注实践性,承认读者最终的目标是完成工作。

# 引——暴风雨前的宁静

一个大门类的技术从来就不是突然出现的。流处理也不例外。

## 流式数据库





## Storm与传统关系型数据库

* 传统关系型数据库先存后计算，而Storm则是先算后存，甚至不存
* 传统关系型数据库很难部署实时计算，只能部署定时任务统计分析
* 关系型数据库重视事务，并发控制



# Storm概览

## 集群架构_static

![image-20210113165127077](C:\Users\Five\Desktop\note\img\image-20210113165127077.png)

* Nimbus
  * 所有信息写在Zookeeper中





* Supervisor nodes





## 运行逻辑_dynamic

* Topology
* Spout
* Bolt





## 数据流动_tuple

* Tuple

数据流的最小单位，很容易联想到关系型数据库的记录。事实上也的确应该算是异曲同工。

* Stream

由若干绵绵不绝的Tuple组成。



# Storm实战

> 0.9.0之前的版本，安装时要安装两个依赖库ZeroMQ和ZMQ。
>
> 由此也可以隐约感受到消息队列和分布式系统的关系。

此处不打算对实战内容逐步、逐代码地去记录。

> Storm核心代码用Clojure实现，使用Java开发Topology，使用Python开发实用程序。

## 安装Storm



## 部署一个Storm Topology



# Features

## 并行度

* Workers（JVMs）
* Executors（threads）
  * 一个Executor线程可以执行多个Task，但一般默认每个Executor只执行一个Task。
* Tasks（Bolt/Spout Instances）



可以在很多地方配置并行度，优先级：defaults.yaml < storm.yaml < topology-specific configuration < internal component-specific configuration < external component-specific configuration.



## Grouping

通过Stream Grouping告诉Topology如何在两个组件之间发送tuple。

* Shuffle Grouping
  * 随机分配，尽量均匀分配给每个bolt
* Fields Grouping
  * 根据元组的特定字段分配，该字段的值相同的元组会分配到相同的Bolts
* All Grouping
  * 广播发送，对于每一个tuple，所有的Bolt都会收到
* Global Grouping
* None Grouping
* Direct Grouping
* Local or shuffle grouping
  * 就近原则，减少网络传输压力和时延
* Custom Grouping



## 消息可靠处理机制

一个消息（Tuple）怎样才算完整处理：

* tuple tree不再继续衍生
* Tuple衍生出的树中的每个节点都标记为已处理



Storm利用异或操作完成了极其巧妙的实现（感觉与Hamming Code的一种优雅实现有异曲同工之妙）：

* 一个新的Tuple诞生时分配一个64bit的二进制码。
* 新的子Tuple诞生时也分配一个64bit的二进制码，并与根Tuple的二进制码进行异或。
* 子Tuple完成时，再与根Tuple的64bit二进制码进行依次异或——以此消除了第一次异或的影响（也是异或神奇的地方）
* 当二进制码归零时，代表所有的Tuple任务都完成。

利用这种巧妙方法，不到8字节即可追踪一个Tuple的完成情况。



## Transactional Topology和Trident

顾名思义，与数据库的事务类似，整个Tuple Tree要么都成功，要么都回退到未执行的状态。

> 经典的Storm通过保证每个Tuple至少被处理一次来提供可靠的数据处理，但不保证仅执行一次。

Storm 0.7.0引入了Transactional Topology，可以保证每个Tuple被且仅被处理一次。

Storm 0.9.0抛弃了Transactional Topology，引入

* 串行化调度
* 强顺序batch流





## DRPC





# 应用案例

## 反爬虫







