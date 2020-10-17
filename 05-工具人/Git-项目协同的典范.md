# Git基础操作

## git配置信息

```bash
git config --scope_level config_name config_value
```

其中scope_level可以是local、gobal、system. 

* local的作用域是一个repository
* global的作用域是当前用户
* system的作用域是所有用户。

配置信息的优先级和编程语言的变量名一样，作用域越小越优先。

查看配置信息

```bash
git config --list --scope_level
```

![image-20201017170334504](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201017170334504.png)

如果scope设为global，则会显示特定用户目录下.gitconfig文件的内容。

### 配置name和email

不配置name和Email后续将无法commit，出现如下所示报错

![image-20201017182330102](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20201017182330102.png)

所以需要执行如下命令进行配置

```bash
git config --global user.name "Nickname"
git config --global user.email "youremailaddress"
```



## git管理结构和提交流程

### 仓库管理

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

啊这，就直接rm或者扔回收站。

### git提交流程

![640](https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/640.png)

> 图并不完全准确，如果是clone会在workspace和Repository克隆两份一样的。然后修改workspace的内容。

1. 添加到暂存区index

   ```bash
   git add file_name
   ```

2. 从暂存区提交到本地仓库repository

   ```bash
   git commit -m "commit remarks"
   ```

3. 远程提交到云端

   ```bash
   git push 
   ```



### 关于远程提交

