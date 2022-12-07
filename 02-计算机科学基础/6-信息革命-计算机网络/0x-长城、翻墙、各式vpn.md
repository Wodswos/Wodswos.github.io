* IP Blocking
* DNS Poisoning
* 

# 典中典案例：无法连接到 Github 的诊断步骤

## 网页端无法访问

检查（ping）和设置 （hosts） DNS

先看能不能 ping 通 github.com

## 设置代理





## Git bash 依旧无法 clone 和 push

查了各种资料：手动设置 dns、全局代理、`git config --global --unset https.proxy` 等等操作

通过全局代理，网页倒是能访问 github 了，但网页也依旧不能访问特定的资源

git bash 中 clone 依旧是 time out。





# 代理

代理（Proxy）也称网络代理，是一种特殊的网络服务。允许一个终端通过这个服务（器）与另一个终端进行非直接的连接。



## 代理模式

* 全局代理







# VPN

VPN的隧道协议主要有四种，[PPTP](https://en.wikipedia.org/wiki/Point-to-Point_Tunneling_Protocol)、[L2TP](https://en.wikipedia.org/wiki/Layer_2_Tunneling_Protocol)、[IPSec](https://en.wikipedia.org/wiki/IPsec)和[SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security)，其中`PPTP`和`L2TP`协议工作在OSI模型的第二层，又称为二层隧道协议；`IPSec`是第三层隧道协议；而`SSL`是工作在OSI会话层之上的协议，如果按照TCP/IP协议模型划分，即工作在应用层。



## 代理 vs vpn



代理工作在 OSI 模型的应用层，或者更狭义地来讲，就是管浏览器（或者说 web，或者说 HTTP，或者说 tcp/udp:80/443）的那点流量。

VPN 在操作系统级别工作（PPTP 和 L2TP 协议工作在数据链路层，IPSec 工作在网络层，SSL 工作在会话层），



> VPN：Virtual Private Network
>
> VPS：Virtual Private Server
>
> **The main difference between a VPN and a VPS is that a VPN is a privacy technology, and a VPS is a server you can rent for hosting.**
>
> 即 vps 是云服务器，而不是一种网络连接技术。这个词中文倒是比英文歧义小得多。









# OpenVPN

OpenVPN is a full-featured SSL VPN which implements OSI layer 2 or 3 secure network extension using the industry standard SSL/TLS protocol, supports flexible client authentication methods based on certificates, smart cards, and/or username/password credentials, and allows user or group-specific access control policies using firewall rules applied to the VPN virtual interface. OpenVPN is not a web application proxy and does not operate through a web browser.



> 



## OpenVPN Cloud





## 





[^1]:How the Great Firewall discovers hidden circumvention servers https://www.youtube.com/watch?v=QBp6opkcxoc
[^2]:The Internet Censorship bibliography https://censorbib.nymity.ch/
[^3]:https://en.wikipedia.org/wiki/OpenVPN