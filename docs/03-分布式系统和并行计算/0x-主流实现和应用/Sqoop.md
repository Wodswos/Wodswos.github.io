> 讽刺的是，我的这门课考试的前一天，Sqoop退役了，Move into the Attic。

> 确实也没啥好讲的内容，很表面、很浅显的一个工具罢了。

* 多数使用hadoop技术的处理大数据业务的企业，有大量的数据存储在关系型数据中
* 由于没有工具支持，对hadoop和关系型数据库之间数据传输是一个很困难的事。

Apache Sqoop(TM) is a tool designed for efficiently transferring bulk data between [Apache Hadoop](http://hadoop.apache.org/) and structured datastores such as relational databases.

# Sqoop的架构

所有的导入导出，其底层都转化为了MapReduce任务

## C/S架构

还是这个说烂了的C/S架构，



# 基本使用

## 安装和部署

> JDK和Hadoop的安装是前提。

* 编辑`sqoop-env.sh`文件
  * `cp sqoop-env-template.sh sqoop-env.sh`
  * 修改以下两行
    * `export HADOOP_COMMON_HOME=$HADOOP_HOME`和`export HADOOP_MAPRED_HOME=$HADOOP_HOME`
* 拷贝`mysql-connector-java-5.0.7-bin.jar`到`$SQOOP_HOME/lib`目录下

> 虽然实际操作中报关于HBase、Hcatalog、Zookeeper的Warning，但我直接无视。

## 命令行

命令基本格式如下

```bash
sqoop tool-name [tool-arguments]
```

其中Tool主要有

* codegen: Generate code to interact with database records
* create-hive-table: Import a table definition into Hive
* eval: Evaluate a SQL Statement and display the results
* export
* help
* import
* import-all-tables
* import-mainframe
* job
* list-databses
* list-tables
* merge
* metastore
* version





## Tools详解

所有Tool的调用既可以写成`sqool codegen`的形式，也可以直接用在bin目录下的`sqool-codegen`命令

### import

| Argument                          | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ |
| `--append`                        | Append data to an existing dataset in HDFS                   |
| `--as-avrodatafile`               | Imports data to Avro Data Files                              |
| `--as-sequencefile`               | Imports data to SequenceFiles                                |
| `--as-textfile`                   | Imports data as plain text (default)                         |
| `--as-parquetfile`                | Imports data to Parquet Files                                |
| `--boundary-query <statement>`    | Boundary query to use for creating splits                    |
| `--columns <col,col,col…>`        | Columns to import from table                                 |
| `--delete-target-dir`             | Delete the import target directory if it exists              |
| `--direct`                        | Use direct connector if exists for the database              |
| `--fetch-size <n>`                | Number of entries to read from database at once.             |
| `--inline-lob-limit <n>`          | Set the maximum size for an inline LOB                       |
| `-m,--num-mappers <n>`            | Use *n* map tasks to import in parallel                      |
| `-e,--query <statement>`          | Import the results of *`statement`*.                         |
| `--split-by <column-name>`        | Column of the table used to split work units. Cannot be used with `--autoreset-to-one-mapper` option. |
| `--split-limit <n>`               | Upper Limit for each split size. This only applies to Integer and Date columns. For date or timestamp fields it is calculated in seconds. |
| `--autoreset-to-one-mapper`       | Import should use one mapper if a table has no primary key and no split-by column is provided. Cannot be used with `--split-by <col>` option. |
| `--table <table-name>`            | Table to read                                                |
| `--target-dir <dir>`              | HDFS destination dir                                         |
| `--temporary-rootdir <dir>`       | HDFS directory for temporary files created during import (overrides default "_sqoop") |
| `--warehouse-dir <dir>`           | HDFS parent for table destination                            |
| `--where <where clause>`          | WHERE clause to use during import                            |
| `-z,--compress`                   | Enable compression                                           |
| `--compression-codec <c>`         | Use Hadoop codec (default gzip)                              |
| `--null-string <null-string>`     | The string to be written for a null value for string columns |
| `--null-non-string <null-string>` | The string to be written for a null value for non-string columns |



## Arguments

Note that generic Hadoop arguments are preceeded by a single dash character (`-`), whereas tool-specific arguments start with two dashes (`--`), unless they are single character arguments such as `-P`.

### Common arguments

| Argument                             | Description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| `--connect <jdbc-uri>`               | Specify JDBC connect string                                  |
| `--connection-manager <class-name>`  | Specify connection manager class to use                      |
| `--driver <class-name>`              | Manually specify JDBC driver class to use                    |
| `--hadoop-mapred-home <dir>`         | Override $HADOOP_MAPRED_HOME                                 |
| `--help`                             | Print usage instructions                                     |
| `--password-file`                    | Set path for a file containing the authentication password   |
| `-P`                                 | Read password from console                                   |
| `--password <password>`              | Set authentication password                                  |
| `--username <username>`              | Set authentication username                                  |
| `--verbose`                          | Print more information while working                         |
| `--connection-param-file <filename>` | Optional properties file that provides connection parameters |
| `--relaxed-isolation`                | Set connection transaction isolation to read uncommitted for the mappers. |



### Generic Hadoop 

```
Generic Hadoop command-line arguments:
(must preceed any tool-specific arguments)
Generic options supported are
-conf <configuration file>     specify an application configuration file
-D <property=value>            use value for given property
-fs <local|namenode:port>      specify a namenode
-jt <local|jobtracker:port>    specify a job tracker
-files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
-libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
-archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute machines.

The general command line syntax is
bin/hadoop command [genericOptions] [commandOptions]
```







## 其他

也可以将配置参数写入文本文件中，如下所示，

```
import
--connect
jdbc:mysql://localhost/db
--username
foo
# 还可以穿插注释
```

随后在命令行运行sqoop并使用该文本文件作为参数

```bash
sqoop --options-file /users/homer/work/import.txt --table TEST
```

其效果和`sqoop import --connect jdbc:mysql://localhost/db --username foo --table TEST`相同







# Sqoop2

* ​	Latest cut of Sqoop2 is 1.99.7（版本号还没正式到2也说明还在beta阶段）
  * Sqoop2 is not intended for production depoloyment.
* Sqoop2和Sqoop1之间几乎没有兼容性可言。



* 它引入的sqoop Server，便于集中化的管理Connector或者其它的第三方插件
* 多种访问方式：CLI、Web UI、REST API
* 它引入了基于角色的安全机制，管理员可以在sqoop Server上配置不同的角色。





[^1]:Sqoop官网https://sqoop.apache.org/
[^2]:宇晨棒棒的 https://www.jianshu.com/p/ec9003d8918c
[^3]:Sqoop官方文档 https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html