# Typora

这个不多说了

个人习惯还是在本地写，不喜欢特定网络平台的写作。而Typora绝对是最好的Markdown编辑器——之一。

> 2020年10月4日更：
>
> **我草泥马的，灯下黑啊**
>
> Typora本身就支持导出HTML、PDF多种格式导出，数学公式渲染好，排版也整齐……
>
> 我他妈还浪费那么多时间在外面找那么多妖艳贱货，我对不起你啊Typora！

但Typora导出要手动一个一个去export，文件数量一多就很蠢，每次修改文档再次手动导出更蠢了。

问Typora官方，官方很礼貌回复谢谢建议，以后会考虑添加批量导出，也没说以后是多久。

> 2020年10月17日更：
>
> 花了很多时间搞pandoc，再次抛弃Typora，选择用Pandoc批量处理，野花还是香啊。

> 2020年12月7日更：
>
> typora回信表示会在v1.0（v1.0大概就是正式发行了叭）中推出命令行导出功能，也就意味着批处理成为可能。
>
> 虽然回信各种祝福和期待（目前是v0.9.96），但心里mmp：折腾了半天的Pandoc，最后可能会弃用。





# 图片云端存储

给自己的本地图片存放路径也定个规范，比如所有图片统一存放在某一目录下，按章节-本章节第N张编号。

> 后来发现根本不用编号，照片不重名就行，编号完全是自找没事，看似整齐，实则吃力不讨好

最后发布的时候统一把所有的所有picture的路径替换为阿里云OSS服务的URL

> 小声bb一句，Windows和Linux默认路径分别用斜杠和反斜杠确实有点nt，关键是现在Windows下两种斜杠还混用了，该夸你兼容呢，还是夸你兼容呢。



## 阿里云OSS介绍

[阿里云对象存储服务官方文档](https://help.aliyun.com/product/31815.html)

![image-20201003145947185](C:/Users/Five/Desktop/note/img/00-01.png)



## PicGo

![image-20201003160022102](C:/Users/Five/Desktop/note/img/00-02.png)



……其实吧，设完之后发现自己的流程中不太需要PicGo，自己手动批量上传到阿里云也很方便……毕竟我不是一开始就在文章里就用阿里云oss的URI，而是先用本地路径，最后发布的时候批量替换的。

所以PicGo的功能对我而言收益不大，各位视情况使用。



另外，其实pandoc支持将图片一并打包（用base64存储）……图片云端存储可能有点多此一举。

但一方面，我个人的云服务器带宽很小，传图片也慢，所以用阿里云OSS还是会快一点，而且！我不想之前费那么多功夫在OSS上是无用功，哈哈，所以还是保留用OSS（即html文件里的图片还是用链接的形式，而不是base64直接存储）。

# 静态网站生成工具

比较有名地静态网站生成工具里，Hugo是Go的，Hexo是JavaScript的，Jekyll是Ruby的，欺我大Python无人嘛？

## Pelican

- Write content in [reStructuredText](http://docutils.sourceforge.net/rst.html) or [Markdown](https://daringfireball.net/projects/markdown/) using your editor of choice
- Includes a simple command line tool to (re)generate site files
- Easy to interface with version control systems and web hooks
- Completely static output is simple to host anywhere

### Quick Start

```bash
pip install "pelican[markdown]" -i https://pypi.tuna.tsinghua.edu.cn/simple
```

啪的一下，很快啊。然后进入要创建静态网站的目录

```bash
pelican-quickstart
```

可以一路回车，用默认设置。



## 其他

### Hugo

一路配置下来，还算比较简单，毕竟是带编译器的正经语言。但效果就……差强人意。

对数学公式不太好……遇到的问题跟Hexo比较像，但架构看着好像要比Hexo清晰多了，应该不难解决，但我还是选择直接转投Pelican。

### Jekyll

- [Ruby](http://www.ruby-lang.org/en/downloads/)（including development headers, Jekyll 2 需要 v1.9.3 及以上版本，Jekyll 3 需要 v2 及以上版本）
- [RubyGems](http://rubygems.org/pages/download)
- Linux, Unix, or Mac OS X
- [NodeJS](http://nodejs.org/), 或其他 JavaScript 运行环境（Jekyll 2 或更早版本需要 CoffeeScript 支持）。
- [Python 2.7](https://www.python.org/downloads/)（Jekyll 2 或更早版本）

需要一堆配置，还对Windows不太友好……直接把我劝退。

### Hexo

hexo也算是我入门的第一个静态网站生成工具，但终究……JS复杂的依赖劝退了我。

> update: Hexo，Hugo，Pelican，都TM是什么垃圾，一点都不智能



# 互联网论坛/平台发布

## github pages

当我因为Pandoc和Typora的convert/export功能揪心的时候，想到了github pages，这个我第一个接触的markdown博客，当初还捣鼓了几天，后来没坚持下来。

github.io只需要你上传markdown文档，访问的时候会自动帮你渲染成网页，那我岂不是可以站在巨人肩膀上，借鉴一下github是咋实现这个功能。

刚想到的时候很激动，虽然意味着我又双叒叕灯下黑了，又白绕了很大圈子，但至少能通过github pages把问题解决了不是。

但github.io的数学公式渲染很不如人意。

对于github pages不能渲染数学公式给出的方案大都是先通过工具将数学公式转换为png图像，再在markdown文件中插入png图像。

但是！这显然不是我想要的，所以无疾而终。



## 公式支持

都很差，不如Typora的渲染。

## 多平台发布工具

Openwrite

个人对紧耦合一直很恐惧……这也是为啥用Markdown而不用特定平台（知乎啊、博客园啊、CSDN啊、简书啊）的原因。



# 数学公式渲染

> Typora supports rendering normal mathematics using Tex/LaTeX syntax. The rendering process is processed by [MathJax](https://www.mathjax.org/).

而且pandoc的默认形式好像只支持typora内的行内公式，而不支持独立模式。同时\$符号后不能跟数字和空格……有点离谱。

而且pandoc渲染的公式和Typora自带的渲染效果……很不一样，总之原生的pandoc着实没有Typora效果好。

官方文档如下：

> Anything between two `$` characters will be treated as TeX math. The opening `$` must have a non-space character immediately to its right, while the closing `$` must have a non-space character immediately to its left, and must not be followed immediately by a digit. Thus, `$20,000 and $30,000` won’t parse as math.

但用Typora难道要手动一个个导出嘛，那也太蠢了。



# Manubot

无意间看到的一个Workflow，感觉思路跟我很像，但项目还停留在比较初级的阶段……学他们代码，还不如我自己来。



# Sphinx







# 其他

## 幻灯片

Markdown能导出PDF、HTML、docx了，那能导出PPT吗

可以，其中一个解决方案就是通过HTML中转（不过不是严谨意义上的PPT，而是网页版幻灯片）。

Markdown到HTML无需赘述了，关键就是html的幻灯片播放——revealJS。

不过目前也没用幻灯片的需求，所以就只在这里先记录一下，万一以后用到了可以查自己的文档。

