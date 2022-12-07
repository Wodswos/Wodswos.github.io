# 基础信息

## 版本

### 内核版本

[官网](https://www.kernel.org)

### 发行版本

* Red Hat Enterprise
* Fedora，也由Red Hat发行，版本较新，稳定性较差
* CentOS
* Debian，与Ubuntu一样拥有图形化界面，适合PC
* Ubuntu



广义的Debian是指一个致力于创建自由操作系统的合作组织及其作品，由于Debian项目众多内核分支中以Linux宏内核为主，而且 Debian开发者 所创建的操作系统中绝大部分基础工具来自于GNU工程 ，因此 “Debian” 常指Debian GNU/Linux。

非官方内核分支还有只支持x86的Debian GNU/Hurd（Hurd微内核），只支持amd64的Dyson（OpenSolaris混合内核）等。这些非官方分支都存在一些严重的问题，没有实用性，比如Hurd微内核在技术上不成熟，而Dyson则基础功能仍不完善。

Ubuntu基于Debian发行版和Gnome桌面环境（也用过Unity桌面环境），是一个以桌面应用为主的Linux操作系统。



# Linux文件目录[^1]

![](C:/Users/Five/Desktop/note/img/d0c50-linux2bfile2bsystem2bhierarchy.jpg)

![](C:/Users/Five/Desktop/note/img/image-20220705150236469.png)

* `/bin`

bin 是 Binaries (二进制文件) 的缩写, 这个目录存放着最经常使用的命令，如`cat`、`chmod`、`chown`、`date`、`mv`、`mkdir`、`cp`、`bash`等等。

* `/sbin`

s是Super User的意思，即Superuser Binaries，存放的是系统管理员使用的系统管理程序。常见的指令包括：fdisk, fsck, ifconfig, init, mkfs等等。

* `/boot`

这里存放的是启动 Linux 时使用的一些核心文件，包括一些连接文件以及镜像文件。

* `/etc`

etc 是 Etcetera(等等) 的缩写,这个目录用来存放所有的系统管理所需要的配置文件和子目录。

 一般来说，这个目录下的各档案属性是可以让一般使用者查阅的，但是只有root有权力修改。 FHS建议不要放置可执行档(binary)在这个目录中。

* `/lib`

lib 是 Library(库) 的缩写这个目录里存放着系统最基本的动态链接共享库，其作用类似于 Windows 里的 DLL 文件。几乎所有的应用程序都需要用到这些共享库。

* `usr`

usr是unix shared resources的缩写，用户的很多应用程序和文件都放在这个目录下，类似于Windows下的program files目录。

注意区分`/bin`、`/usr/bin`、`/user/local/bin`三个目录

* `/opt`

opt 是 optional(可选) 的缩写，这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。 

* `/var`

var 是 variable(变量) 的缩写，这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

* `/root`

系统管理员(root)的家目录。 之所以放在这里，是因为如果进入单人维护模式而仅挂载根目录时，该目录就能够拥有root的家目录，所以我们会希望root的家目录与根目录放置在同一个分区中。

* `/home`

非系统管理员的家目录存放于此，如`/home/Stacey`，就是用户Stacey的目录

常用符号`~`代表当前使用者的家目录

* `/dev`

在Linux系统上，任何装置与周边设备都是以档案的型态存在于这个目录当中。 只要通过存取这个目录下的某个档案，就等于存取某个装置。比要重要的档案有`/dev/null`、`/dev/zero`、`/dev/tty`、`/dev/lp`、`/ dev/hd`、`/dev/sd`等等

* `/tmp`

这是让一般使用者或者是正在执行的程序暂时放置档案的地方。这个目录是任何人都能够存取的，所以你需要定期的清理一下。当然，重要资料不可放置在此目录啊。 因为FHS甚至建议在开机时，应该要将/tmp下的资料都删除。

* `/sys`

这是 Linux2.6 内核的一个很大的变化。该目录下安装了 2.6 内核中新出现的一个文件系统 sysfs 。

sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的 proc 文件系统、针对设备的 devfs 文件系统以及针对伪终端的 devpts 文件系统。



还有其他如挂载floppy、cdrom等可移除硬件的`/media`和`/mnt`、Redhat/CentOS特有的`/selinux`、存放一些服务启动之后需要提取的数据的`/srv`（如`/srb/www`）等目录就不详述了





linux为什么访问设备数据先要mount? - 醉卧沙场的回答 - 知乎 https://www.zhihu.com/question/524667726/answer/2437952746







[^1]:https://www.runoob.com/linux/linux-system-contents.html
