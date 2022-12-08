MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。



# 架构

## 关于用户

MongoDB好像默认可以无用户名和密码登录

```bash
mongod -f /mongodb/etc/mongo.conf --auth
```

`--auth`表示启动授权，需要帐号密码才能访问

`auth=true`可以加到mongo.conf配置文件里面去进行统一管理

# 基本操作

## 安装、启动和关闭

先安装libcurl和openssl的依赖

```bash
sudo yum install libcurl openssl
```

在MongoDB官网获取下载链接

![image-20210622092253969](C:\Users\Five\Desktop\note\img\image-20210622092253969.png)

```bash
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-4.4.6.tgz
```

在`/etc/profile`中添加环境变量

```bash
export MONGODB_PATH=/root/software/mongodb_4.4.6
export PATH=$PATH:$MONGODB_PATH/bin
```



启动服务，并指定数据目录`/var/lib/mongo`和日志目录`/var/log/mongodb/mongod.log`，`--fork`类似于`&`，使其在后台运行。

```bash
mongod --dbpath /root/data/lib/mongo --logpath /root/data/log/mongodb/mongod.log --fork=true
```

也可以绑定IP和端口

```bash
./mongod --dbpath=/path/mongodb --bind_ip=10.10.10.10 --port=12345 & 
```

这些内容都可以以配置文件的形式保存

```
dbpath=/var/lib/mongo
logpath=/var/log/mongodb/mongodb
bind_ip=0.0.0.0
port=27017
fork=true
logappend=true
```

最后是关闭mongod，也要指定相应的配置文件，或在命令行给出参数（否则会按mongod它自己猜测的默认值来）

```bash
mongod --shutdown -f /opt/mongo-4.4.6/bin/mongod.conf
```





## 命令行交互

MongoDB的命令行（控制台）是一个JavaScript Shell

数据库的操作语法基本和SQL类似（当然因为是NoSQL，所以肯定会在数据操作上有不同）



### Database

创建和使用数据库都是SQL的`USE`指令（如不存在则创建并使用，如存在则使用）

`show databases`可以缩写为`show dbs`

删除命令是`db.dropDatabase()`



### Collection

类似于关系型数据库中Table的概念

连查看Collection的命令也是`show tables`或者`show collections`

```javascript
use database_name
db.createCollection(name,options)
```

插入数据到不存在的集合中时也会自动创建集合。

删除集合可用如下命令

```js
db.collection_name.drop()
```



### Document

Document的结构和JSON类似，MongoDB 使用`insert()`或`save()`方法向Collection中插入Document

```js
db.COLLECTION_NAME.insert(Document)
// or db.COLLECTION_NAME.save(document)
// Document具体内容可如下所示
db.Collection_name.isnert(age:18)
```

3.2 版本之后新增了`db.collection.insertOne()`和`db.collection.insertMany()`。

查询集合内所有Document命令如下所示：

```js
db.collection.find().pretty()
```

其中`pretty()`表示格式化呈现（记得BeautifulSoup中也有类似的函数）





## 报错和debug



