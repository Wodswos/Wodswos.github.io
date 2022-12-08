# 数据查询和分析

## Analysis Service

Analysis Services 是在决策支持和业务分析中使用的分析数据引擎（Vertipaq）。 它为商业智能（BI）、数据分析和报告应用程序（例如 Power BI、Excel、Reporting Services 和其他数据可视化工具）提供企业级语义数据模型功能。

* 一个引擎三个平台

Analysis Services 在三个不同的平台上提供企业级语义建模、监管、生命周期和数据管理： Azure 中的云、在本地和 SQL Server ，并且在 Analysis Services 引擎的环境下， Power BI Premium 工作区和数据集。 







## 机器学习服务

Machine Learning Services，害，作为最终考研目标就是机器学习的男人，最后还是决定选了这个Features，了解了解也好。



## Data Quality Services

自动化的系统通常无法处理不正确的数据，需要另外花费时间和人力进行人工处理。 不正确的数据会对数据分析、报告、数据挖掘和仓库造成不良影响。

DQS 是一种知识驱动型解决方案，该解决方案通过计算机辅助方式和交互方式来管理数据源的完整性和质量。 

使用 DQS 可以发现、生成和管理有关您数据的知识。 然后可以使用该知识执行数据清理、匹配和事件探查。 还可以在 DQS 数据质量项目中利用引用数据访问接口的基于云的服务。

![](C:/Users/Five/Desktop/note/img/dqs-process.gif)



# 多维表达式MDX

语法元素，标识符，数据类型，MDX表达式，运算符，函数，注释，保留关键字，成员、元组和集

## MDX、XMLA、DAX

XMLA（XML for Analysis）



# 数据迁移和加载

## Integration Services

SQL Server Integration Services 是用于生成企业级数据集成和数据转换解决方案的平台。 使用 Integration Services 可解决复杂的业务问题，具体表现为：复制或下载文件，加载数据仓库，清除和挖掘数据以及管理 SQL Server 对象和数据。

Integration Services 可以提取和转换来自多种源（如 XML 数据文件、平面文件和关系数据源）的数据，然后将这些数据加载到一个或多个目标。

Integration Services 包括一组丰富的内置任务和转换，用于生成包的图形工具和可在其中存储、运行和管理包的 Integration Services 目录数据库。

可以使用图形 Integration Services 工具来创建解决方案，而无需编写单行代码。 也可以编写广泛的 Integration Services 对象模型以编程方式创建包，并对自定义任务和其他包对象进行编码。



### Scale Out Worker

### Scale Out Master



## PolyBase Query Service

借助 PolyBase，SQL Server 实例可处理从外部数据源中读取数据的 Transact-SQL 查询。 SQL Server 2016 及更高版本可以访问 Hadoop 和 Azure Blob 存储中的外部数据。 从 SQL Server 2019 开始，现在可以使用 PolyBase 访问 SQL Server、Oracle、Teradata 和 MongoDB 中的外部数据。

> 毕竟本科专业还挂着个大数据（虽然水的一逼），故选择添加并学习此Feature。

# 扩展工具

命令行提示符实用程序、数据库优化顾问、分布式重播、SQL Server配置管理器、SQLCMD、SSB诊断、SQL Server Data Tools、SSMS、SQL Server Profiler等等。

## 分布式重播Distributed Replay

> The Microsoft SQL Server Distributed Replay feature helps you assess the impact of future SQL Server upgrades. You can also use it to help assess the impact of hardware and operating system upgrades, and SQL Server tuning.

## SQL Browser

如果一个物理服务器上面有多个SQL Server实例，那么为了确保客户端能访问到正确的实例，所以自SQL Server 2005提供了一个新的Browser服务。

SQL Server服务器缺省使用TCP1433端口。如果多实例同时启动，一般就只有一个实例能占用1433端口了。

SQL Server 浏览器程序以 Windows 服务的形式运行。SQL Server 浏览器侦听对 Microsoft SQL Server 资源的传入请求，并提供计算机上安装的 SQL Server 实例的相关信息。SQL Server 浏览器可用于执行下列操作：

- 浏览可用服务器列表
- 连接到正确的服务器实例
- 连接到专用管理员连接 (DAC) 端点

# SQL Azure

![image-20201111110927921](C:\Users\Five\Desktop\note\img\image-20201111110927921.png)

  QL Azure (旧称 SQL Server Data Services 或 SQL Services) 是由微软SQL Server 2008为主，建构在Windows Azure云操作系统之上，运行云计算 (Cloud Computing)的关系数据库服务 (Database as a Service)，是一种云存储(Cloud Storage)的实现，提供网络型的应用程序数据存储的服务。

## Azure

Microsoft Azure是微软基于云计算的操作系统，原名“Windows Azure”，和Azure Services Platform一样，是微软“软件和服务”技术的名称。

Microsoft Azure的主要目标是为开发者提供一个平台，使开发者能使用微软全球数据中心的储存、计算能力和网络基础服务。

Azure服务平台包括了以下主要组件：Microsoft Azure，Microsoft SQL数据库服务，Microsoft .Net服务，用于分享、储存和同步文件的Live服务，针对商业的Microsoft SharePoint和Microsoft Dynamics CRM服务。

> Azure对标AWS，是一个服务平台

## SQL Azure



# 巨硬，YYDS

微软，毕竟是业界领导者，yyds，出品的Access和Excel大名鼎鼎。

## Power BI

![](C:\Users\Five\Desktop\note\img\3c62b6d0810117ac863dc344b2e5ac7f_1440w.jpg)

Power BI的核心理念就是让我们用户不需要强大的技术背景，只需要掌握Excel这样简单的工具就能快速上手商业数据分析及可视化。

> 哟呵，真就程序员还没跨界抢饭碗，自己的饭碗就要被别人跨界抢了呗。

## Power Pivot

Power Pivot是微软Power BI 系列工具的大脑，负责建模分析。有人说它是过去20年Excel里最好的新功能。可以轻松处理各个量级的数据。





