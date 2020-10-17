# Storm集群

### 物理部署

##### 配置基本环境

JDK，Zookeeper等

##### 修改config文件storm.yaml

##### 启动storm

```bash
nohup storm nimbus/supervisor/ui >/dev/null 2>&1 &
```

后台运行且不输出信息（重定向到Linux黑洞）。

### 节点组成

##### Nimbus

The master in Storm cluster.

* fail-fast

It can be restarted without having any effects on the already running tsaks on the worker node.

Unlike hadoop that all running jobs are left in an inconsistent state when JobTracker dies.

##### Supervisor

The worker nodes in Storm cluster.

##### Zookeeper Cluster

Storm uses a Zookeeper cluster to coordinate various process.

* zookeeper中有workerbeats节点记录所有worker的心跳。
* assignments节点中保存了所有Topology的任务分配信息、代码存储目录、任务间的关联信息
  * Supervisor轮询此节点领取任务
* 还有backpressure,erros,blobstore,leader-lock,logconfigs,nimbuses,supervisors等节点记录各种信息

![image-20200929085535057](\picture\x-01.png)

# Storm Topology

### 结构

##### Spout

The source of tuples in a storm topology. It is responsible for reading or listening to data from  an external source.

* Reading from a logfile
* Listening for new messages in a queue

And then publishing them - emitting. Here are some important methods of spout:

* nextTuple(): Define the logic of reading data and emiting them.
  * backtype.storm.spout.ISpoutOutputCollector
* ack():Invoked by storm when it identifies that tuple has not been processed successfully.
* fail()
* open()

##### Bolt

A bolt is the processing powerhouse of a Storm topology and is responsible for transforming a stream.

* execute(Tuple input): The most important method which is executed for each tuple that comes through the subscribed input streams.

### 提交

##### 本地提交

Storm topologies run on local machine in a single JVM. 

This mode is used for the testing and debugging of a topology.

```java
LocalCluster cluster = new LocalCluster();
cluster.submitTopology(TOPOLOGY_NAME, conf, builder.createTopology());
Thread.sleep(2000);
cluster.shutdown();
```



##### 远程提交

1. Storm提交后，把代码首先存放到Nimbus节点的inbox目录下，生成配置文件stormconf.ser、序列化Topology代码文件在stormdist目录下。
2. 设定Topology所关联的Spouts和Bolts，可同时设置executor和task数目。
3. Nimbus将工作提交到zookeeper。
4. Supervisor轮询zookeeper集群，领取自己的任务



```java
StormSubmitter.submitTopology(TOPOLOGY_NAME,conf,builder.createTopology());
```



### 执行

![](/picture/x-02.png)

##### Worker（进程级）

##### Excutor和Task（线程级）

每个executor只会运行1个topology的1个component(spout或bolt)的task，但task的数量没有限制（只要是同一个component），storm默认是1个component只生成1个task，executor线程里会在每次循环里顺序调用所有task实例



##### 运行命令

```bash
storm jar StormTopology.jar mainclass [args]
```



##### Topology管理

杀死/停用/启用一个topo

```bash
storm kill/deactivate/activate topology_name [-w wait_time]
```

负载平衡，会先停用拓扑，然后重新分配worker，重启拓扑

```bash
storm rebalance topology_name 
[-w wait_time] 
[-n worker_amount] 
[-e component_name=executer_amount]
```



### 简单Topology实现

##### maven依赖

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>storm.test</groupId>
  <artifactId>stormsample</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>stormsample</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>

<dependency> 
	<groupId>org.apache.storm</groupId> 
	<artifactId>storm-core</artifactId> 
	<version>1.2.3</version> 
	<scope>provided</scope>
</dependency>

  </dependencies>

<repositories>
        <repository>
                <id>clojars.org</id>
                <url>http://clojars.org/repo</url>
        </repository>
</repositories>


<build> 
	<plugins> 
		<plugin>
			<artifactId>maven-assembly-plugin</artifactId>
			<version>2.2.1</version>
			<configuration> 
				<descriptorRefs>
					<descriptorRef>jar-with-dependencies </descriptorRef> 
				</descriptorRefs> 
				<archive> 
					<manifest> <mainClass /> </manifest>
				 </archive>
			</configuration>
		 	<executions> 
				<execution>
				<id>make-assembly</id>
				<phase>package</phase>
				<goals>
					 <goal>single</goal>
				</goals>
				</execution>
			</executions>
		</plugin>
	 </plugins>
</build>

</project>

```



##### Spout、Bolt

SpoutDemo

```java
package storm.test;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MySpout extends BaseRichSpout {
    private static final long serialVersionUID = 1L;
    private SpoutOutputCollector spoutOutputCollector;
    private static final Map<Integer,String> map = new HashMap<Integer, String>();
    static {
        map.put(0,"huawei");
        map.put(1,"google");
        map.put(2,"ali");
        map.put(3,"tencent");
        map.put(4,"baidu");
    }

    public void open(Map map, TopologyContext topologyContext, SpoutOutputCollector spoutOutputCollector) {
        this.spoutOutputCollector = spoutOutputCollector;
    }

    public void nextTuple() {
        final Random random = new Random();

        int randomNumber = random.nextInt(5);
        spoutOutputCollector.emit(new Values(map.get(randomNumber)));
    }

    public void declareOutputFields(OutputFieldsDeclarer outputFieldsDeclarer) {
        outputFieldsDeclarer.declare(new Fields("company"));
    }
}
```

Bolt Demo

```java
package storm.test;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Tuple;

import java.util.Map;

public class MyBolt extends BaseRichBolt {
    private static final long serialVersionUID = 1L;

    public void prepare(Map map, TopologyContext topologyContext, OutputCollector outputCollector) {
    }

    public void execute(Tuple tuple) {
        String company = tuple.getStringByField("company");
        System.out.println("company " + company);
    }

    public void declareOutputFields(OutputFieldsDeclarer outputFieldsDeclarer) {

    }
}
```

##### Topology Submission (Local)

```java
package storm.test;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;

public class MyTopology {
    public static void main(String[] args) throws InterruptedException {
        TopologyBuilder builder = new TopologyBuilder();

        builder.setSpout("Random Company Generator",new MySpout(),2);
        builder.setBolt("Company Printer",new MyBolt(),4).shuffleGrouping("Random Company Generator");

        Config config = new Config();
        config.setDebug(true);


        LocalCluster cluster  = new LocalCluster();

        cluster.submitTopology("my Topology",config,builder.createTopology());

        Thread.sleep(1000);
        cluster.killTopology("my Topology");
        cluster.shutdown();

    }
}
```



##### Topology Submission (Real-Distributed/Remote)

```java
package storm.test.demo1;

import org.apache.storm.Config;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.AlreadyAliveException;
import org.apache.storm.generated.AuthorizationException;
import org.apache.storm.generated.InvalidTopologyException;
import org.apache.storm.topology.TopologyBuilder;

public class MyTopology {
    public static void main(String[] args) throws InterruptedException, InvalidTopologyException, AuthorizationException, AlreadyAliveException {
        TopologyBuilder builder = new TopologyBuilder();

        builder.setSpout("RandomGenerateCompany",new MySpout(),2);
        builder.setBolt("CompanyPrinter",new MyBolt(),4).shuffleGrouping("RandomGenerateCompany");

        Config config = new Config();
//        config.setDebug(true);
        config.setNumWorkers(3);
        StormSubmitter.submitTopology(args[0],config, builder.createTopology());
    }
}
```

Submit

```bash
storm jar jar_name.jar [TopologyMainClass] [TopologyName] [OtherArgs]
```

Submit之后就无休止地跑起来了，（第一次地时候没想到这么猛，虚拟机用的动态分配内存差点爆掉），Deactivate topology:

```bash
storm deactivate topologyName 
```

彻底杀死topology，使之不再占用内存：

```bash
storm kill topologyName
```

Storm中经常用topologyName去对topology进行管理。

所以名字最好取得规律一些。



### The Parallelism of a Topology