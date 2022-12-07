# 信息革命



计算机掀起了算力的革命，互联网（可能要加个硬盘）则彻底地颠覆了信息领域。在我的理解里，信息革命指的是互联网而不是计算机。（当然，互联网是计算机组成的）

在互联网之前，信息的传递都需要借助于物理实体：从木简到书本，无一不如此。

虽然信息的承载体在不断改进，单位体积的实体成本越来越低，承载的信息越来越多。

但传统的存储介质（如书本）还是太贵了，而且实体的物流速度…即使有了现代交通工具的助力…但又怎么可能跟电磁波的光速比呢？而信息依附于实体，自然也很慢。

> 这么说也不太准确，电话和电报的诞生，已经使得光速传递信息成为可能。但电话和电报仅限于点对点，频率和内容远远没法和现在的互联网相比。

> 以文字类（中文）的信息为例进行成本比较
>
> （多媒体方面，图片的差距可能比文字略小，但传统设备几乎压根不具备传递视频等其他多媒体信息的能力，所以就不考虑了）
>
> * 信息时代前后的存储成本比较：
>
> 对传统设备宽容点，往价低了算，1元 = 10W字的印刷成本+纸张成本，对信息设备苛刻点，1000元 = 一个5T的移动硬盘（一般5T机械硬盘再贵也不会超过1000元）
>
> 按上述假设，那么1000元够印刷1亿字。而对于硬盘，即使是用UTF8存储（3个字节存储一个汉字字符），也能存储$5 \times 1024^4 \div 3 \approx 1.8 \times 10^{12}$字，是传统印刷的18000倍。
>
> * 信息时代前后的传输成本比较：
>
> 带宽……其实很难全面比较，（一辆满载书籍/硬盘的列车其带宽其实会很大）.
>
> 懒得写了，以后有空填坑。但想也知道电磁波比传统物流便宜太多了。
>
> 姑且算让让传统媒体，打个平局。
>
> * 信息时代前后的传输速度比较：
>
> 及时性上，光速自然完全碾压。
>
> 
>
> 综合来看，互联网为代表的信息时代已经完成了全方面的碾压。



# 互联网简史

## 从ARPANET到Internet[^3]

* 1960s，Paul Baran和Donald Davies等人（独立）开始进行关于packet switching的研究
* 1960s-1970s，NPL Network的包交换设计被广泛应用到各种网络设计
  * NPL指National Physical Laboratory（伦敦）
* 1969年，ARPANET（阿帕网）开始尝试在UCLA和SRI两地之间建立只有两个节点的网络连接。
  * 1971年，ARPANET节点增加至15个，节点基本限于美国境内
  * 1973年，通过卫星建立了到NORSAR（挪威）的连接
* 1974年，Vint Cerf和Bob Kahn用`internet`作为`internetwork`的缩写，随后被广泛采用。
* 1981年，在NSF的资助下，ARPANET继续扩张

* 1982年，Internet Protocol Suite提出，也即TCP/IP
  * 其核心和基础是Transmission Control Protocol（TCP）和Internet Protocol（IP）两份协议
* 1983年，TCP/IP协议称为ARPANET的标准协议
* 1985年，NSF围绕六个大型计算机中心建设NSFNET

* 1990年，ARPANET任务完成，正式关闭
* 1991年，美国政府将因特网主干交给私人公司经营，并开始收费



## 基于ISP的Internet

> 一般小写的internet泛指由多个计算机网络互联而成的网络，这些网络间的通信协议可以是任意的、
>
> 大写的Internet特指当前全球最大的计算机网络，采用TCP/IP协议簇作为通信的规则。

* 1993年，NSFNET逐渐被若干商用因特网主干网代替
  * 政府机构不再负责因特网的运营，转而由各种ISP运营
* 1994年，万维网（WWW）在欧洲核子中心诞生
* 1995年，NSFNET停止运作，因特网彻底商业化



### ISP网络结构

![](C:/Users/Five/Desktop/note/img/1200px-Internet_Connectivity_Distribution_&_Core.png)

* 单一国际交换ISP结构
  * 由这个网络中心的ISP负责在各国的ISP之间进行协调通信
  * 很多国家的ISP都想做这个global ISP，毕竟有钱赚
* 多个国际交换ISP结构
  * 只在本国活动的local ISP叫做Tier 2，如中国三大运营商，大陆没有Tier 1的ISP
    * 好像也有说中国电信和联通升级到T1的？？
  * 美国的Sprint、AT&T、Lumen Technologies等，德国的DTGC，瑞典的Telia Carrier，日本的NTT Communications，中国香港的PCCW Global、意大利的Telecom Italia Sparkle等等都是Tier 1的ISP
* 多级层连结构
* 对等和多重访问结构
* 网络公司自己当ISP，自建数据中心，不对外提供服务，自给自足，如Google



> CAIDA, Center for Applied Internet Data Analysis
>
> 有很多关于互联网的很有意思的数据

### 因特网标准化工作

* 因特网所有的RFC（Request For Comments）技术文档都公开并免费下载
* 任何人都可以随时用电子邮件对某个RFC发表建议



Internet Society, ISOC, 因特网协会，负责对因特网进行全面管理

* IAB，Internet体系结构委员会，负责管理Internet有关协议的开发
* IETF，Internet工程部，负责研究中短期工程问题
* IRTF，Internet研究部，从事理论方面的研究，或解决长期性的问题

> http://www.evolutionoftheweb.com/ 一个宝藏网站。以图的方式记录了互联网（主要是HTTP和WWW）发展的历程。
>
> 很遗憾，好像打不开了。

# OSI参考模型

> In 1983, the CCITT and ISO documents were merged to form *The Basic Reference Model for Open Systems Interconnection,* usually referred to as the *Open Systems Interconnection Reference Model*, *OSI Reference Model*, or simply *OSI model*. 
>
> It was published in 1984 by both the ISO, as standard [ISO 7498](https://en.wikipedia.org/wiki/ISO_7498), and the renamed CCITT (now called the Telecommunications Standardization Sector of the [International Telecommunication Union](https://en.wikipedia.org/wiki/International_Telecommunication_Union) or [ITU-T](https://en.wikipedia.org/wiki/ITU-T)) as standard X.200.

![](C:/Users/Five/Desktop/note/img/705728-20160424234826351-1957282396.png)

![](C:/Users/Five/Desktop/note/img/705728-20160424234827195-1493107425.png)



> Open System Interconnection Reference Model
>
> 由国际标准化组织提出，一个试图使计算机在世界范围内互通网络的标准框架。

> 对等通信：为了使数据分组从源传送到目的地，源端OSI模型的每一层都必须与目的端的对等层进行通信，这种通信方式称为对等层通信。在每一层通信过程中，使用本层自己协议进行通信。
>
> 即在每一层，都可以（或者说应该）忽略其他层的细节，而只专注于当前层的任务。

| OSI参考模型 | 使命                                                         |
| ----------- | ------------------------------------------------------------ |
| 物理层      | 参考模型中的最底层，定义系统的电气、机械、过程和功能标准     |
| 数据链路层  | 用字节组成帧，并以**帧**为传输的基本单位，为网络层提供差错控制和流量控制服务 |
| 网络层      | 用帧组成数据包，并以**数据包**为传输的基本单位，负责数据包从源网络传输到目标网络的路由选择工作 |
| 传输层      | 用数据包组成段，并以**段**为传输的基本单位，提供面向连接或非面向连接的数据传递。 |
| 会话层      |                                                              |
| 表示层      |                                                              |
| 应用层      |                                                              |







> The OSI model is still used as a reference for teaching and documentation; however, the OSI protocols originally conceived for the model did not gain popularity.
>
> Some engineers argue the OSI reference model is still relevant to cloud computing[^1]. Others say the original OSI model doesn't fit today's networking protocols and have suggested instead a simplified approach[^2].



![](C:/Users/Five/Desktop/note/img/96c62019cfc58d6f67f6c5701f8cbb61.jpg)



# 学习和参考资源

《网络通信原理》

《图解HTTP》

《从实践中学习TCP/IP协议》

《趣谈网络协议》



## 一些好文

一台主机上只能保持最多 65535 个 TCP 连接吗？ - 闪客sun的回答 - 知乎 https://www.zhihu.com/question/361111920/answer/1861488526

https://www.bilibili.com/video/BV1Ki4y1g7f2 【回形针PaperClip】你打电话时究竟发生了什么？

万字45张图详解计算机网络基础知识 - 网络工程师笔记的文章 - 知乎 https://zhuanlan.zhihu.com/p/370764245

33 张图详解 TCP 和 UDP ：打通网络和应用的中间商 - 网工Fox的文章 - 知乎 https://zhuanlan.zhihu.com/p/383723040

20张图深度详解MAC地址表、ARP表、路由表 - 网络工程师笔记的文章 - 知乎 https://zhuanlan.zhihu.com/p/401928579





[^1]: ["An OSI Model for Cloud"](https://blogs.cisco.com/cloud/an-osi-model-for-cloud). *Cisco Blogs*. 24 February 2017. Retrieved 16 May 2020.
[^2]:  Taylor, Steve; Metzler, Jim (23 September 2008). ["Why it's time to let the OSI model die"](https://www.networkworld.com/article/2276158/why-it-s-time-to-let-the-osi-model-die.html). *Network World*. Retrieved 16 May 2020.
[^3]: https://en.wikipedia.org/wiki/Internet
[^4]: https://www.jianshu.com/p/787d3fd4a69b
[^5]: https://en.wikipedia.org/wiki/Tier_1_network
