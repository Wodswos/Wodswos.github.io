Flume Agent Souce Sink 绑定 Channel

Channel里的Event按照轮询发送sink到目的地



# Flume概述

![image](C:/Users/Five/Desktop/note/img/1228818-20180505130552077-1235640783.png)

Flume 在0.9.x and 1.x之间有较大的架构调整，1.x版本之后的改称Flume NG（Next Generation），0.9.x的称为Flume OG（Original Generation）。

## 架构

### Data Flow model

A Flume event is defined as a unit of data flow having a byte payload and an optional set of string attributes. 

A Flume agent is a (JVM) process that hosts the components through which events flow from an external source to the next destination (hop).

![image](C:/Users/Five/Desktop/note/img/DevGuide_image00.png)

### Comlex flows

感觉Flume的multi-hop flows有点Storm的味道。





### 可靠性

Flume提供3种数据可靠性选项

* End-to-end
  * 磁盘日志和接收端Ack的方式，保证Flume接收的数据到达目的地
* Store on failure
  * 在目的地不可用时，数据保持在本地硬盘
  * 进程出现问题可能会丢失部分数据
* Best effort



### 其他

* 伸缩性：三大组件Collector、Master、Storage tier均可伸缩
* 配置一致性：利用Zookeeper和gossip，保证配置数据的一致性
* 扩展性：自定义Source、Sink等



## 安装部署

* 修改环境变量
* conf目录下`cp flume-env.sh.template flume-env.sh`，并修改文件中的JAVA_HOME
* 用`flume-ng version`验证



### 创建服务器端

新建conf文件指定服务器端配置

```bash
# example.conf: A single-node Flume configuration
# Name the components on this agent 
a1.sources = r1 
a1.sinks = k1 
a1.channels = c1
# Describe/configure the source 
a1.sources.r1.type = netcat 
a1.sources.r1.bind = localhost 
a1.sources.r1.port = 44444
# Describe the sink 
a1.sinks.k1.type = logger
# Use a channel which buffers events in memory 
a1.channels.c1.type = memory 
a1.channels.c1.capacity = 1000 
a1.channels.c1.transactionCapacity = 100
# Bind the source and sink to the channel 
a1.sources.r1.channels = c1 
a1.sinks.k1.channel = c1
```

用如下命令运行

```bash
../bin/flume-ng agent --conf conf/ --conf-file example.conf --name a1 Dflume.root.logger=INFO,console
```

其中`--conf`or`-c`指定的是配置目录，`--conf-file`or`-f`指定agent的配置文件

另一份服务器端配置示例

```bash
# Define a memory channel called ch1 on agent1 
agent1.channels.ch1.type = memory 
agent1.channels.ch1.capacity = 100000 
agent1.channels.ch1.transactionCapacity = 100000 
agent1.channels.ch1.keep-alive = 30 
#define source monitor a file 
agent1.sources.avro-source1.type = exec 
agent1.sources.avro-source1.shell = /bin/bash -c 
agent1.sources.avro-source1.command = tail -n +0 -F /home/storm/tmp/id.txt 
agent1.sources.avro-source1.channels = ch1 
agent1.sources.avro-source1.threads = 5 
# Define a logger sink that simply logs all events it receives 
# and connect it to the other end of the same channel. 
agent1.sinks.log-sink1.channel = ch1 
agent1.sinks.log-sink1.type = hdfs 
agent1.sinks.log-sink1.hdfs.path = hdfs://192.168.1.111:8020/flumeTest 
agent1.sinks.log-sink1.hdfs.writeFormat = Text 
agent1.sinks.log-sink1.hdfs.fileType = DataStream 
agent1.sinks.log-sink1.hdfs.rollInterval = 0 
agent1.sinks.log-sink1.hdfs.rollSize = 1000000 
agent1.sinks.log-sink1.hdfs.rollCount = 0 
agent1.sinks.log-sink1.hdfs.batchSize = 1000 
agent1.sinks.log-sink1.hdfs.txnEventMax = 1000 
agent1.sinks.log-sink1.hdfs.callTimeout = 60000 
agent1.sinks.log-sink1.hdfs.appendTimeout = 60000 
# Finally, now that we've defined all of our components, tell 
# agent1 which ones we want to activate. 
agent1.channels = ch1 
agent1.sources = avro-source1 
agent1.sinks = log-sink1
```



### 创建客户端

由于示例中的服务端srouce type是netcat，所以客户端可以通过一个简单的`talnet`命令实现

```bash
talnet localhost 44444
```



# FLume组件详解

* Event：一个数据单元，带有一个可选的消息头，可以是日志记录、 avro 对象等
  * 对于文本文件通常为一行记录
* Flow：Event 从源点到达目的点的迁移的抽象



## Agent



### Source



* Avro Source
* Exce Source：指定某Shell命令的stdout作为输入
  * 如常用的`tail -F [File]`
  * 可以实现实时传输，但在 flume 不运行和脚本错误时，会丢数据，也不支持断点续传功能，且由于没有“记忆”，所以不知道上一次传到哪里了
  * 有execStream的扩展
* Spooling Directory Sourc
  * 监听某目录，该目录不可包含子目录，拷贝到该目录的文件不可再打开编辑
  * 实践中可以结合log4j使用，将文件分割机制设为1分钟一次，并拷贝到spool的监控目录
  * Flume 在传完文件之后，将会修改文件的后 缀，变为.COMPLETED（后缀也可以在配置文件中灵活指定）
* NetCat Source
* Taidir Source
  * Watch the specified files, and tail them in nearly real-time once detected new lines appended to the each files. If the new lines are being written, this source will retry reading them in wait for the completion of the write.
* Syslog Source

* * 有Syslog TCP Source和Syslog UDP Source

* JMS Source
  * 从Java Message Service获取数据输入Channel
* Kafka Source：内置Kafka Comsumer，从Kafka读取某个topic数据写入Channel
* 其他的还有如HTTP Source、HDFS Source等



如果内置的Source无法满足需要， Flume还支持自定义Source。





### Channel



* Memory Channel：更高的吞吐，更低的数据完整性保障
* JDBC Channel
  * 内置支持Derby
* File Channel
  * 持久化所有的事件，并将其存储到磁盘 中
  * 即使 Java 虚拟机宕掉，或者操作系统崩溃或重启，再或者事件没有在管道中成功 地传递到下一个代理（agent），这一切都不会造成数据丢失。
* Psuedo Transaction Channel
  * 用于测试
* Spillable Memory Channel



### Sink

* HDFS sink
* Logger sink
  * 
* Avro sink
  * 数据被转换成 Avro Event，然后发送到配置的 RPC 端口上
  * Thirft Sink类似
* IRC Sink
  * 在IRC上进行回放
* File Roll sink
  * 存储数据到本地文件系统
* Null sink
  * 丢弃所有数据
* HBase sink

Flume Sink在设置存储数据时，可以向文件系统中，数据库中，hadoop中储数据，在日志数据较少时，可以将数据存储在文件系中，并且设定一定的时间间隔保存数据。在日志数据较多时，可以将相应的日志数据存储到Hadoop中，便于日后进行相应的数据分析。

## Collector

用于对数据进行聚合。



# Setup[^1]

## Single Agent



### Trigger

* SizeTrigger
  * 在调用 HDFS 输出流写的同时，count 该流已经写入的大小总和，若超过 一定大小，则创建新的文件和输出流，写入操作指向新的输出流，同时 close 以前的输 出流
* TimeTrigger
  * 开启定时器，当到达该点时，自动创建新的文件和输出流，新的写入重定 向到该流中，同时 close 以前的输出流





## Data ingestion



## Multi-agent flow

> In order to flow the data across multiple agents or hops, the sink of the previous agent and source of the current hop need to be avro type with the sink pointing to the hostname (or IP address) and port of the source.

![](C:/Users/Five/Desktop/note/img/UserGuide_image03.png)

## Consolidation

> A very common scenario in log collection is a large number of log producing clients sending data to a few consumer agents that are attached to the storage subsystem. For example, logs collected from hundreds of web servers sent to a dozen of agents that write to HDFS cluster.

![](C:/Users/Five/Desktop/note/img/UserGuide_image02.png)



## multiplexing the flow

 ![](C:/Users/Five/Desktop/note/img/UserGuide_image01.png)

# Flume vs Kafka

有各种极端对立的观点

* 有的认为Flume和Kafka差别很大，使用场景差异也很大
* 有的认为Flume和Kafka本身是很相似的系统，都能无压力传输很大的数据量



1. Kafka是pull based, 如果你有很多下游的Data Consumer，用Kafka；
2. Kafka有Replication，Flume没有，如果要求很高的容错性(Data High Availability)，选kafka；
3. 需要更好的Hadoop类产品接口，例如HDFS，HBase等，用Flume。



## 整合Flume和Kafka

* 自定义KafkaSink
* 配置Agent
* KafkaSpoutTest
* KafkaTopologyTest



## Storm-Flume-Kafka[^2]

![](C:/Users/Five/Desktop/note/img/650365-20190429173653211-1906011450.jpg)



采集层：实现日志收集，使用负载均衡策略

消息队列：作用是解耦及不同速度系统缓冲

实时处理单元：用Storm来进行数据处理，最终数据流入DB中

展示单元：数据可视化，使用WEB框架展示



![](C:/Users/Five/Desktop/note/img/650365-20190429173726685-968002116.jpg)

# Debug日志

java.lang.OutOfMemoryError: Java heap space

在conf目录的flume-env.sh文件中可以设置JAVA_OPTS。





[^1]:http://flume.apache.org/releases/content/1.9.0/FlumeUserGuide.html
[^2]:https://www.cnblogs.com/cac2020/p/10791843.html