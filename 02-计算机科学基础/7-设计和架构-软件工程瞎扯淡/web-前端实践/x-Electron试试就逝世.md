



# Electron概述

Electron改名自Atom-shell项目。

![image-20201027195239846](C:/Users/Five/Desktop/note/img/image-20201027195239846.png)



## Electron架构

因为Electron使用了Chromium来展示web页面，所以Chromium的多进程也会很自然地应用到Electron。

![image-20201027201158932](C:/Users/Five/Desktop/note/img/image-20201027201158932.png)



### 整合 Chromium 和 Node.js

NodeJS事件循环基于libuv，但Chromium基于Message bump

* 选择一：Chromium集成到NodeJS：用libuv实现Message Bump
  * Browser主进程的工程量会很浩大
* Electron：NodeJS集成到Chromium

![image-20201117124548740](C:\Users\Five\Desktop\note\img\image-20201117124548740.png)



## Electron环境搭建

### Node.js

因为没有用nvm，所以直接从[官网](https://nodejs.org/en/)下载Node.js，版本14.15.1LTS

过程没啥好说的，命令行验证是否安装成功。

![image-20201120175335382](C:\Users\Five\Desktop\note\img\image-20201120175335382.png)

### 获取Electron

之后安装Electron，基本上npm都会用[淘宝的镜像](https://developer.aliyun.com/mirror/NPM)

```bash
set ELECTRON_MIRROR=http://npm.taobao.org/mirrors/electron/
# windows设置环境变量的命令是set
# 或者可以用cnpm、也可以给npm直接设置registry
npm install -g electron
```

#### 可附加选项

`--arch=ia32`和`--platform=win32`，基于32位开发和打包，这样得到的结果在32位和64位下都可以用，只需维护一个版本即可。

`--save-dev`，会将模块依赖写入devDependencies 节点。运行`npm install`初始化项目时，会将模块下载到项目目录下。



也可以在[网页端镜像](https://npm.taobao.org/mirrors/electron)选择版本下载Electron zip包解压缩后将路径添加到系统环境变量。





# Electron初体验（无疾而终）

![image-20201117143547791](C:\Users\Five\Desktop\note\img\image-20201117143547791.png)

## 主要文件

### package.json

`package.json`是Node.js项目的配置文件，可以通过`npm init`创建一个package.json文件

```json
{
  "name": "tomato",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "SE Group",
  "license": "ISC"
}
```



### main.js

`main.js`是应用的启动入口。



### index.html

`index.html`是应用的展示界面。

