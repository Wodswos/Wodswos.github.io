传统意义上，消息引擎/队列负责的是消息的分发，而不太负责消息的处理。

# 消息引擎和Kafka基础概念

## 消息引擎系统

相比于“队列”这个词（可能更简洁直观），“引擎系统”可能更能贴切地反映出Kafka的核心作用——消息传递。

> wikipedia:
>
> 消息引擎系统是一组规范。
>
> 企业利用这组规范在不同系统之间传递语义准确的消息，实现**松耦合**的**异步式**数据传递。



### 为什么是消息引擎系统

削峰填谷。



### 消息格式

成熟的解决方案：CSV，XML，JSON。

或是大厂开源的序列化框架，如Google的Protocol Buffer或Facebook的Thrift。

Kafka使用纯二进制的字节序列。



### 消息传输协议和模型

Kafka同时支持点对点模型和发布/订阅模型。

#### 点对点模型

即消息队列模型。系统A的消息只能被指定的系统B接收。

#### 发布/订阅模型



## Kafka和流处理

Apache Kafka是消息引擎系统，也是一个分布式流处理平台。[^1]

Kafka是LinkedIn公司内部孵化的项目，LinkedIn开始有强烈的强实时数据处理的需求。

（都是社交软件，Twitter为Storm收购BackType，LinkedIn有同样的需求情理之中）

* 数据正确性不足。数据的收集靠轮询，但轮询的时间间隔只能靠经验和启发式算法。
* 系统高度定制化，耦合度高，维护成本高



Kafka救世。0.10.0以前的Kafka被定位为一个分布式、分区化且带备份功能的提交日志服务。

设计初旨：

* 提供一套API实现Producer和Consumer
* 降低网络传输和磁盘存储开销
* 实现高扩展性架构



流处理组件——Kafka Stream。Kafka某种程度上是和Spark、Storm、Flink同等级的实时流处理平台。

> Tyler：流处理要最终替代它的“兄弟”批处理需要具备两点核心优势
>
> * 正确性
> * 提供能够推导时间的工具。

正确性是批处理的强项，对于流处理其难点在于提供精确一次处理语义。主流的大数据流处理框架都宣称实现了精确一次处理语义，但这仅限于其框架内，而不是端到端的。

但因为所有的数据流转和计算都在Kafka内部完成，故Kafka可以实现端到端的精确一次处理语义。



Kafka定位也和和Spark、Storm、Flink不太一样，不正面比较流计算的框架，保证自己端到端的价值。



## Kafka逻辑架构

### C/S架构

Broker: Kafka服务端，接受和处理Clients的请求，并对消息持久化

> 单个Broker应该算是Kafka集群服务端代理，而不是完整的Kafka集群服务。
>
> 所有的Broker程序加在一起才算是Kafka集群服务端?



Clients: Producer和Consumer统称clients，相对于Kafka服务而言。

Producer：向主题发布消息的应用程序

Consumer：订阅主题消息的应用程序



### Topic和Partition

每个Topic划分为若干分区，类似于HBase中的Region。

每个分区对应一组有序的消息日志。

Producer的每条消息发送到Topic下的某一Partition，Consumer会订阅所有的Partition。



### Broker和Replica

领导者副本LeaderReplica和追随者副本FollowerReplica，前者提供服务，后者负责备份。

副本是定义在分区层级下的概念（即同一个Topic不同分区的信息的副本是分开的），即副本$\in$分区。

> 一个副本向上属于某一Broker和某一分区。
>
> 但分区不属于某一特定Broker，Broker也不属于特定分区。



![](C:/Users/Five/Desktop/note/img/x-k-02.png)



#### Kafka数据持久化

消息日志：磁盘上一个只能追加写（Append-Only，提高写入速度）的物理文件。

> 日志段机制
>
> 日志进一步细分为日志段，写满一个日志段后自动切分一个新的日志段，并封存旧的日志





## Kafka版本

### Apache Kafka

只提供读写磁盘文件的连接器，其他外部系统需要自己实现

没有提供任何监控框架或工具。（有开源监控框架可以帮助，如Kafka manager）

### Kafka版本号变动

0.8版本引入副本机制

0.9版本增加了基础的安全认证、权限功能，引入Kafka Connect组件

0.10引入了Kafka Stream，升级为分布式流处理平台

0.11提供幂等性Producer API以及事务API，消息格式重构

1.0和2.0主要集中于Kafka Streams的改进。

### Kafka商业版本

Confluent Kafka、Cloudera/Hortonworks Kafka



# Kafka集群部署和运行

## 集群参数配置

> 参数配置不是必须的,如果仅仅想先运行起来,可以直接跳到下一节

[官网](http://kafka.apache.org/25/documentation.html#configuration)

### Broker参数

* 配置存储信息
  * lod.dirs：指定Broker需要适合用的若干文件目录
    * 如/home/kafka1,/home/kafka2...
    * 没有默认值,需要手动指定
* Broker连接
  * listeners
    * 告诉外部连接者通过什么协议访问指定主机名和端口开放的Kafka服务
  * advertised.listeners



zookeeper，记录集群的Broker，在哪里运行，创建了哪些Topic，每个Topic 有多少分区，以及Leader副本的位置信息等。

![image-20200930164937520](C:/Users/Five/Desktop/note/img/x-k-08.png)





### bootstrap-server



### Topic



## 运行Kafka

> 这里已经提前搭建好并运行了zookeeper集群
>
> Kafka默认配置文件里zookeeper的端口为localhost:2181

### 启动Kafka Server

```bash
$ bin/kafka-server-start.sh config/server.properties
```

![image-20200929195147035](C:/Users/Five/Desktop/note/img/x-k-03.png)



zookeeper集群上挂起了许多与Kafka相关的节点，brokers，consumers……其实我也不太清楚每个节点都是啥，还有storm混入其中（因为storm没关）



### 创建topic

```bash
$ kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```

![image-20200929195658355](C:/Users/Five/Desktop/note/img/x-k-04.png)

关于--bootstrap-server参数

![image-20200930163046908](C:/Users/Five/Desktop/note/img/x-k-07.png)



### Write some events into the topic

```bash
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
```

![image-20200929200002392](C:/Users/Five/Desktop/note/img/x-k-05.png)



### Read events by Consumer

```bash
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

![image-20200929200219142](C:/Users/Five/Desktop/note/img/x-k-06.png)

妙啊，真的读出来了，就是命令行不能退格还显示成^H符号让我很不爽



## KAFKA CONNECT: Import/Export





## Kafka Stream



# 深入Kafka

## Producer

* Producer怎么知道Topic在哪些个Broker上？而又具体该是分发给哪个Broker？

  * 问Zookeeper吗？可是Producer又该怎么知道Zookeeper搁哪呢？

    > All Kafka nodes can answer a request for metadata about which servers are alive and where the leaders for the partitions of a topic are at any given time to allow the producer to appropriately direct its requests.

* 

## Consumer





## Broker



## 各种参数

* `log.dirs`
  * 如`/home/kafka1,/home/kafka2,/home/kafka3 `
  * 并最好保证这些路径挂载到不同磁盘上，以此提高I/O，也能实现故障转移
    * Kafka1.1版本后，坏掉的磁盘上的数据会自动地转移到其他正常的磁盘上
* `zookeeper.connect`
  * 多套Kafka集群可以共用一个zookeeper。
  * `zk1:2181,zk2:2181,zk3:2181/kafka1`和`zk1:2181,zk2:2181,zk3:2181/kafka2`
    *  chroot 只需要写一次，而且是加到最后的



* `listeners`
  * 告诉外部连接者，通过什么协议访问指定主机名和端口开放的 Kafka 服务





* `auto.create.topics.enable`
  * 当设为True时，向一个不存在的Topic名发送消息时，该Topic会自动生成。
* `unclean.leader.election.enable`
  * 一般来说，数据最新的为leader副本，当数据较新的版本都挂了，该参数决定是否允许进度落后的副本成为leader副本

关于数据

* `log.retention.{hour|minutes|ms}`
  * 如`log.retention.hour=168`表示默认保存 7 天的数据
* `log.retention.bytes`
  * 设为-1表示无限大
* `message.max.bytes`







[^1]:极客时间《Kafka核心技术与实战》