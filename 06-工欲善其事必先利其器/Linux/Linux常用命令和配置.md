![image-20220705150236469](C:\Users\Five\Desktop\note\img\image-20220705150236469.png)

# 任务管理



* `systemctl`
* `service`

## systemd

![](C:/Users/Five/Desktop/note/img/bg2016030703.png)

* `systemctl`是 Systemd 的主命令，用于管理系统。
* `systemd-analyze`命令用于查看启动耗时。
* `hostnamectl`命令用于查看当前主机的信息。
* `localectl`命令用于查看本地化设置。
* `timedatectl`命令用于查看当前时区设置。
* `loginctl`命令用于查看当前登录的用户。



# 包和应用管理

当Linux环境下需要下载某个应用时，常用的包管理命令为`apt-get`和`yum`

* `apt-get`
  * 建立在dpkg之上的软件管理工具，包格式deb
* `yum`
  * 是RPM提供的更高级工具，包格式rpm



dpkg，Debian Packager，由伊恩·默多克于1993年创建，是一个可以安装、构建、删除及管理 Debian 软件包的命令行工具，用来制作Debian包的工具，同时也可以查看、解压Debian包。

apt，Advanced Packaging Tool，是Ubuntu Linux中的命令行软件包管理工具，用于获取、安装、编译、卸载和查询Deb软件包，以及检查软件包的依赖关系。常用的APT实用程序（命令）是`apt-get`、`apt- cache`、`apt-file`、`apt-cdrom`。

> Ubuntu 16.04引入了新的 `apt`命令（即`apt`命令和APT是两样东西，`apt`命令比`apt-get`等旧命令出现得要晚）。
>
> apt命令的引入是为了解决命令过于分散的问题，它包括了 apt-get 命令出现以来使用最广泛的功能选项，以及 apt-cache 和 apt-config 命令中很少用到的功能。
>
> 现在，`apt install package`命令的使用频率和普遍性甚至逐步超过`apt-get install package`。

RPM最早由 Red Hat 公司制定实施，随后被 GNU 开源操作系统接受并成为很多 Linux 系统 (RHEL) 的既定软件标准。

yum（Yellow dog Update Modifier），是RPM提供的更高级工具，能手动管理RPM的依赖关系。

# 网络配置





# 其他命令

## 解压缩

解压缩工具`tar`

* x：解压，c：压缩
* v：显示信息
* f：指定文件类型为file
* j：gz压缩，z：zip压缩



故常用tar -zxvf

# 常用工具

## Vi/Vim

基础的Vi很粗糙，语法高亮都木的，一般都默认为Vim-Vi IMproved

### 正常模式：初始模式

![Vi/Vim键盘图](C:/Users/Five/Desktop/note/img/01-01.png)

### 编辑模式：正常输入

通过i键（Insert）进入编辑模式，正常输入字符，也可以通过O，A等键进入编辑模式。

ESC返回正常模式。



### 命令模式

通过在正常模式键入冒号":"进入。

q表示quit退出，w表示save保存，!表示强制

wq保存退出，q!退出不保存。

也可以用命令":w new_filename"将文件另存为。

查找‘\’+re

替换%s/find_string/replace_string



### 可视模式

主要应用块可视模式。

