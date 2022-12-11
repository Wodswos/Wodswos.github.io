

HTTP（Hyper Text Transfer Protocol，超文本传输协议）是一个简单的请求-响应协议，它通常运行在TCP之上。

> HTTP通常被译为超文本传输协议，但这种译法并不严谨。严谨的译名应该 为“超文本转移协议”。
>
> https://www.ituring.com.cn/article/1817

HTTP协议运行在应用层，同其他应用层协议一样，是为了实现某一类具体应用的协议（浏览器，服务器默认端口号80/TCP）。

# WWW：HTTP的前世今生

CERN（欧洲核子研究组织）的蒂姆 • 伯纳斯 - 李（Tim BernersLee）博士提出了一种能让远隔两地的研究者们共享知识的设想。

* 把SGML（Standard Generalized Markup Language，标准通用标记语言）作为页面的文本标记语言的HTML（HyperText Markup Language，超文本标记语言）
* 作为文档传递协议的HTTP
  * 即设计HTTP最初的目的是为了提供一种发布和接收HTML页面的方法。
* 指定文档所在地址的URL（Uniform Resource Locator，统一资源定位符）。





```sequence
Client -> Server: TCP请求，三次握手
Client -> Server: HTTP请求
Server -> Client: HTTP响应

```

## HTML



## URL和URI

URL是一种URI的具体实现，不仅唯一标识了资源地址，往往还通过file://或http://等定义了如何访问资源。

只要能唯一标识资源的就是URI，在URI的基础上给出其资源的访问方式的就是URL



## HTTP特点

* HTTP允许传输任意类型的数据对象。传输类型由Content-Type标记
* 无连接。限制每次连接只处理一个请求。服务器处理完请求，并收到客户的应答后，即断开连接
  * 有Cookie和Session作为会话连接的补充
* 无状态。协议对于事务处理没有记忆，后续处理需要前面的信息，则必须重传。





# HTTP报文

以访问个人的博客首页为例，整个过程中一共有如下所示的报文数量：

![image-20201027113913604](C:/Users/Five/Desktop/note/img/image-20201027113913604.png)

接下来以上图中ali报文为例

> 因为我在本地的hosts文件中将ali作为域名解析到了个人的阿里云服务器，所以这里显示报文name为ali

## Request

### 请求行

该报文的请求行为GET / HTTP/1.1

常用请求方法/请求行：

* GET
* POST
* HEAD，类似get请求，但返回的响应没有正文，只有Headers。
* PUT
* DELETE



### 请求头

以上图中的ali那段报文为例，可查看其请求头内容如下

![image-20201027113959461](C:/Users/Five/Desktop/note/img/image-20201027113959461.png)

### 请求正文





## Response

### 状态行

ali报文返回的Status Code: 304

> 如果客户端发送了一个带条件的GET 请求且该请求已被允许，而文档的内容（自上次访问以来或者根据请求的条件）并没有改变，则服务器应当返回这个304状态码。简单的表达就是：服务端已经执行了GET，但文件未变化。

可以看到其他报文返回的Status Code为200.

> 200表示请求已成功，请求所希望的响应头或数据体将随此响应返回。

其他常见的如404，403

> 404，请求失败，请求所希望得到的资源未被在服务器上发现。没有信息能够告诉用户这个状况到底是暂时的还是永久的。
>
> 假如服务器知道情况的话，应当使用410状态码来告知旧资源因为某些内部的配置机制问题，已经永久的不可用，而且没有任何可以跳转的地址。
>
> 404这个状态码被广泛应用于当服务器不想揭示到底为何请求被拒绝或者没有其他适合的响应可用的情况下。

> The HTTP **403** Forbidden client error status response code indicates that the server understood the request but refuses to authorize it.

状态类型

* 1xx-信息型，服务器收到请求，需要请求者继续操作
* 2xx-成功型
* 3xx-重定向
* 4xx-客户端错误，请求包含语法错误或无法完成请求
* 5xx-服务端错误



### 响应头

我个人在服务端选择的Server是Nginx而不是另一主流Apache。所以在响应头会显示Server的类型为Nginx。

此处请求html文件所以显示Content-Type: text/html

> 如果请求的是css文件，会显示Content-Type: text/css

![image-20201027115209942](C:/Users/Five/Desktop/note/img/image-20201027115209942.png)



### 响应正文

因为请求的是一个index.html文件，所以响应正文就是整个html文件。

![image-20201027115441791](C:/Users/Five/Desktop/note/img/image-20201027115441791.png)





# HTTPS

HTTP协议往往是明文传输，在互联网的环境下非常不安全。

特别是一些敏感信息，如账号密码等，使用HTTP传输会非常容易泄露隐私。

- 请求信息明文传输，容易被窃听截取。
- 数据的完整性未校验，容易被篡改
- 没有验证对方身份，存在冒充危险

> HTTPS的默认端口是443，和HTTP的默认端口80不同。



## SSL

一般HTTPS理解为HTTP+SSL(Secure Socket Layer).

> 1996年发布SSL/3.0版本，得到大规模应用
>
> TLS是SSL升级版，1999年，发布了TLS/1.0版本，目前应用最广泛的版本
>
> 2006年和2008年，发布了TLS/1.1版本和TLS/1.2版本

SSL协议位于TCP等传输协议和HTTP等应用协议之间，为数据通信提供安全支持。

```sequence
Client -> Server: 请求HTTPS连接
Server --> Client: 返回证书
Note left of Client: 产生随机数（对称密钥）
Note left of Client: 用公钥将对称密钥加密
Client -> Server: 发送加密后的对称密钥
Note right of Server: 用私钥解密得到对称密钥
Server --> Client: 通过对称密钥加密http通信....
Client --> Server: 通过对称密钥加密http通信....
```



在上述时序图中提到了证书的概念，什么是证书呢？

> B该如何验证A的公钥是否合法，或者是不是真的属于A而不是别人伪造的呢？

## CA证书授权

需要一个权威的中间机构。





[^2]:[A Story about Encrypted communication](http://www.youdzone.com/signature.html) 