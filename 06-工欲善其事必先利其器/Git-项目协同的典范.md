# Git基础信息

## git 配置信息

```bash
git config --scope_level config_name config_value
```

其中scope_level可以是local、gobal、system. 

* local的作用域是一个repository，对应路径为工作目录中的 `.git/config` 文件
* global的作用域是当前用户，对应路径为 `~/.gitconfig` 文件
* system的作用域是所有用户，对应路径为 `/etc/gitconfig` 文件

配置信息的优先级和编程语言的变量名一样，作用域越小越优先。

查看配置信息

```bash
git config --list --scope_level
```

![image-20201017170334504](C:/Users/Five/Desktop/note/img/image-20201017170334504.png)

如果scope设为global，则会显示特定用户目录下.gitconfig文件的内容。

### 配置name和email

不配置name和Email后续将无法commit，出现如下所示报错

![image-20201017182330102](C:/Users/Five/Desktop/note/img/image-20201017182330102.png)

所以需要执行如下命令进行配置（或者可以在创建仓库后再在local作用域下定义name和email）

```bash
git config --global user.name "Nickname"
git config --global user.email "youremailaddress"
```



## git 基本结构和基本流程

### 本地仓库管理

仓库可以通过本地新建和云端克隆已有的仓库

#### 新建git仓库

1. 新建一个空的git仓库

   ```bash
   git init repository_name
   ```

2. 把本地已有代码纳入git管理

   ```bash
   cd project_dir
   git init
   ```

3. 从云端克隆

   ```bash
   git clone https://github.com/user/project.git
   ```

#### 删除仓库

直接rm或者扔回收站。

### git 提交：add、commit、push

![640](C:/Users/Five/Desktop/note/img/640.png)

> 图并不完全准确，如果是 clone 会在 workspace和 Repository 克隆两份一样的。
>
> 然后工作时修改 workspace 的内容。

1. 添加到暂存区index

   ```bash
   git add file_name
   ```

2. 从暂存区提交到本地仓库repository

   ```bash
   git commit -m "commit remarks"
   ```

3. 从本地仓库提交到云端（或者说远程仓库）

   ```bash
   git push remote-host local_branch:remote_branch
   ```



> 如不指定，默认 remote_name为 `origin`
>
> 在默认情况下，`origin`指向的就是你本地的代码库托管在 Github上的版本。如在 terminal 通过 git clone 复制仓库到本地，此时本地仓库会和远程仓库建立连接/映射关系。（没有特殊意义，是一个默认的习惯）

> 当 local_branch 和 remote_branch 相同时，可以合并写为一个 branch_name，即省略冒号后的部分。



### 从远程 clone

除了本地从头创建 git 仓库外，更多的显然是从远程（github） clone 自己所需的项目。

```bash
git clone  https://github.com/Username/Repository_name
```







### .gitignore

`.gitignore`文件告诉Git哪些文件不需要添加到版本管理中。

```
以叹号!表示不忽略匹配到的文件或目录；
以斜杠/开头表示目录；
以星号*通配多个字符；
以问号?通配单个字符
以方括号[]包含单个字符的匹配列表；
```

如

```
/folder_name/	忽略整个文件夹
*.zip	忽略所有zip文件
/folder_name/filename	忽略指定文件

!/folder_name/	不忽略该文件夹
!/folder_name/filename	不忽略指定文件
```



## 其他

```bash
git [command-name] --help
```

如上形式的代码会调出git存储在本地的、关于对应 command-name （如 push、remote 等）的、网页版的帮助文档

> 以前我就觉得，有些帮助文档很长，在命令行显示就显得很累赘。
>
> 但如果为了精简而缩短帮助文档，那显然又使得帮助文档很难起到最好的效果。



# 其他常用命令和操作

## 远程操作（github）

远程当然不只有github，在自己的电脑本地就可以建立一个“远程仓库”，操作与github几乎并无二致。但此处依旧以github为例。

### Remote to local

从远程下载的repository会自带如下config

![image-20201019210326974](C:/Users/Five/Desktop/note/img/image-20201019210326974.png)

于是你可以在验证身份信息后直接git push。

#### git remot

`git remote -v` 可以查看远程仓库映射关系

完整命令信息如下

```bash
git remote [-v | --verbose]
git remote add [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=<fetch|push>] <name> <url>
git remote rename <old> <new>
git remote remove <name>
git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
git remote set-branches [--add] <name> <branch>…
git remote get-url [--push] [--all] <name>
git remote set-url [--push] <name> <newurl> [<oldurl>]
git remote set-url --add [--push] <name> <newurl>
git remote set-url --delete [--push] <name> <url>
git remote [-v | --verbose] show [-n] <name>…
git remote prune [-n | --dry-run] <name>…
git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)…]
```

![image-20201019210741988](C:/Users/Five/Desktop/note/img/image-20201019210741988.png)



### Local to Remote

对于本地创建的新git项目显然是没有自带的远程信息的，也不能用git remote命令。

#### 在Github新建仓库

不赘述了，GUI点点点就完了

#### 给本地仓库设置远程信息

```bash
git remote add remote_name git@github.com:your_repository.git 
```

然后就可以查看remote信息

![image-20201019213957130](C:/Users/Five/Desktop/note/img/image-20201019213957130.png)

#### push

```bash
git push remote_name
```

因为远程仓库新建，还空空如也，所以会有如下报错

![image-20201019214120988](C:/Users/Five/Desktop/note/img/image-20201019214120988.png)

需要新建分支，或者在push的同时创建分支

![image-20201027184846277](C:/Users/Five/Desktop/note/img/image-20201027184846277.png)



## git branch





## 配置 SSH





### git@github.com

ssh 交互的对象（host）是 git@github.com。

```
git push git@github.com:user_name/repository_name branch_name
```







# 安全的网络传输——HTTPS和SSH

https和ssh是github接受的两种clone方式。github某种程度上本就为开源而生（对于public的仓库），所以通过http和ssh都可以clone任意repository.

用http在push的时候是需要验证用户名和密码的。而 ssh在push的时候，是不需要输入用户名的，如果配置SSH key的时候设置了密码，则需要输入密码的，否则直接是不需要输入密码的。

网络环境是很危险的，可能有各种各样的攻击、伪造、中间人、信息被篡改等可能。那应该怎么实现网络的安全传输呢？

SSH和HTTPS是两种安全的传输协议（就目前的计算水平而言）。

## RSA算法和数字签名

第一次看到RSA算法的感觉就是……这tm是魔法吗？

毕竟作为一个数学并不太好的工科生，自然不可能对数论有啥认知。

在正常的认知里，对称加密算法是直观而天经地义的，怎样加的的密，就要怎样解，解铃还须系铃人。加密加了x解密就要减x，加密乘了x解密就要除以x。

直到Diffie-Hellman密钥交换算法的出现，作为一种崭新构思，可以在不直接传递密钥的情况下，完成解密。

### Diffie-Hellman密钥交换算法

#### 离散对数

1. 原根：对于数$a$和数$p$，若有$a,a^2,a^3,...,a^{p-1}$对于$p$取余都有不同的值（即对应从1到p-1的一种排列），则称$a$是素数$p$的原根。
2. 离散对数：对于数$b$和数$i$，若有$b=a^i\%p$，则称$i$为$b$的（以$a$为基数模$p$的）离散对数。

已知$i$，计算$b$是很简单的；而反过来，已知$b$，计算$i$却是很困难的。

>  即对满足同一个式子的两个量，正向和反向的两个计算过程对于计算机而言计算量却不是一个量级的

Diffie-Hellman密钥交换算法有效性依赖于计算离散对数的难度。

#### 算法原理

1. 公开信息：选定素数和原根$p,a,(a<p)$
2. A、B各自选定任意两个数$X_a,X_b$
3. 计算$Y_a,Y_b$：$Y_a=a^{X_a}\%p,Y_b=a^{X_b}\%p$，并公开$Y_a,Y_b$
4. A通过计算$K = Y_b^{X_a} \% p$得到密钥，同理B通过计算$K = Y_a^{X_b} \% p$得到密钥

又已知，通过$Y_a,Y_b$反向得到离散对数$X_a,X_b$是困难的。所以外人因为没有$X_a,X_b$之一，无法得到密钥，

> 简单证明A、B两人计算得到的密钥相同：
>
> $K_a = Y_b^{X_a} \% p = (a^{X_b} \% p)^{X_a}\%p = a^{X_a * X_b}\%p = Y_a^{X_b} \% p =K_b$



### 数学先验知识

参见数学系列-代数和结构-图论



### 能被破解吗

当然能，困难归困难，但本质上依旧只是计算复杂度的问题，而不是可能与不可能的问题。

以11代core i7为例，仅仅只需要计算大概……

### 数字签名

[A Story about Encrypted communication](http://www.youdzone.com/signature.html)





防止被篡改。

### 数字证书

#### CA证书授权



## SSH的使用

ssh是一个传输协议，一个加密的传输协议，通常基于神奇的RSA算法。

### 私钥和公钥

公钥和私钥相对的，是可以互换的。

在实际操作中，openssl生成两个密钥，你选择公开（一般都默认id_rsa.pub文件）的那个即为公钥，自留的（id_rsa）即为私钥。

如果你愿意，你也可以将id_rsa重命名为id_rsa.pub并作为公钥保存到其他地方，将id_rsa.pub重命名为is_rsa作为私钥。



> 如果你自己实现了算法，当然没问题。
> 但是如果你是用Openssl之类的就不行。因为Openssl把生成公、私钥用的东西和私钥全部存在私钥pem里了。并且openssl的公钥`e`固定为65537。
>
> from https://segmentfault.com/q/1010000002932436



> 理论上，KeyGen得到的是(e,d,n)，(e,d)哪个作为公钥都是可以的，你公开的那个就是公钥，保留的那个就是私钥。
> 但实现中出于性能考虑，e是选好的e=65537（一开始是e=3，但是有小指数攻击的问题），这样e就只能作为公钥了。
>
> 同样from https://segmentfault.com/q/1010000002932436

### 生成SSH密钥对

指定用rsa算法，

```
ssh-keygen -t rsa
```

然后连续回车，不需要（通常）指定保存路径、passphrase

![image-20201020104448339](C:/Users/Five/Desktop/note/img/image-20201020104448339.png)

此时会在userhome/.ssh/目录下生成两个文件，即公钥和私钥。

### authorized_keys

保存所有公钥的地方，将之前生成的公钥追加写入该文件中。

```bash
cd .ssh/
cat id_rsa.pub >> authorized_keys
```

就可以畅通无阻的本地循环了，即

```bash
ssh localhost
```

当然，这并没有啥卵用，只能自己逗自己玩。

需要将id_rsa.pub保存到你所要登陆的服务器/github上。

> 



# 关于开源

## 开源协议

![img](C:/Users/Five/Desktop/note/img/9375552-fbabeb4870d4d42b.png)

