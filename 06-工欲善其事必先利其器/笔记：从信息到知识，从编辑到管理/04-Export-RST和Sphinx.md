# RST

ReStructedText

## RST简介

文件扩展名 RST 有 二 种文件类型，并且与 六 种不同的软件程序相关联，但主要相关联软件程序是由 **Microsoft Corporation**开发的 **Microsoft Notepad**。 通常这些被格式化为 **ReStructuredText File**。 这些文件分为 **Text Files** 或 GIS Files。 在大多数情况下，这些文件属于 **Text Files**。

Windows、 Mac和 Linux 操作系统可用于查看 RST 文件。 这些程序通常可以在桌面（以及一些移动）设备上找到，使您能够查看并有时编辑上述格式文件。 普及性为“低”时，普通人通常不会使用这些文件。

如果您想了解有关 RST 文件和打开它们的软件的更多信息，请参阅下面的其他详细信息。 此外，如果您在打开 RST 文件时遇到问题，可以学习如何对其进行基本故障排除。



## Markdown和RST

官方的说法直截了当， Markdown 就是个 text-to-HTML 的工具。从一开始，Markdown 就确立了它与 HTML 的亲缘性。

Markdown 包含两个部分：

1. 文本结构化格式，也就是标记语言
2. 另外与之配套的生成 HTML 的 perl 程序。

作为标记语言， Markdown 的目标很明确，就是为了更简单的写 html 。相比与 Markdown ， ReST 显然是经过精心设计的。

ReST的目标是，**建立一套标准文本结构化格式用以将文档转化为有用的数据格式。**

Pythoner给出了更具体的阐述：

1. Readable，是可阅读的，ReST的原文本必须可以很容易的直接阅读而不需要了解ReST的标记语法。
2. Unobtrusive，不突兀的，ReST 所使用的标记应该是尽量简单并且不突兀的。越是常用的标记越应该简单和不碍眼的。不太常用的标记，或者是表达特殊意义的标记应该鲜明。
3. Unambiguous，没有歧义的，标记规则是确定的，不能再重载定义，对于给定的一个输入，只有一个可能的输出，包括输出错误。
4. Unsurprising，不出乎预期的，非“魔法”的，标记语言可以不输出不想输出的内容。所以，需要一个方式（标记）作为标记不期望输出标记之用。比如，当你想要向别人展示ReST源代码时，你要标记这块ReST源码不需要被结构化。
5. Intuitive， 直观的，标签应该尽可能的容易被记住。人们可以在文档中直接使用。
6. Easy，简单，

> Markdown成功也离不开Github的主推。
>
> 再后续的话，不管是MarkdownPad还是Typora，Markdown生态越来越好，就算有这样那样的缺点，也已经彻底成为主流的标记语言了。



## 语法



### 关于段落

用`::`表示`literal block`

RST表格的语法比Markdown更精致一些……但那只是因为Markdown太差，而不是RST优秀，可能标记语言确实不适合表格（庆幸有所见即所得的Typora等编辑器）。

![image-20201202214653259](C:\Users\Five\Desktop\note\img\image-20201202214653259.png)

### Inline Markup

斜体和粗体的表示与Markdown无异。

RST的超链接有多种方法，如

```reStructuredText
External hyperlinks, like `Python
<http://www.python.org/>`_.
```

另一种和Markdown的文献引用有点像，不是在原地给出超链接地址，而是锚和信息分开。



### 各种list

* 最基础的Bullet List和Enumerated List，语法也跟Markdown类似
* Definition List
* Field List：类似Author等
* Option List：就类似-v --version这种option

![image-20201202212319385](C:\Users\Five\Desktop\note\img\image-20201202212319385.png)

### 图片

语法`.. image:: image\image_name.jpg`

> 虽然RST确实不错的样子，但也点到为止，年轻人我讲武德，我还爱我的Markdown。



# Sphinx

> sphinx，直译狮身人面像。
>
> 通常有两两种指代，一种是搜索引擎，一种是基于Python的文档工具。

sphinx是一种基于Python的文档工具，它可以令人轻松的撰写出清晰且优美的文档，由Georg Brandl在BSD许可证下开发。新版的Python3文档就是由sphinx生成的，并且它已成为Python项目首选的文档工具，同时它对C/C++项目也有很好的支持。更多详细特性请参考[spinx官方文档](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html)。

```bash
sphinx-quickstart
```

然后就是一系列配置

```
Separate source and build directories (y/n) [n]:
Project name:
Author name:
Project release []:
Project Language [en]: zh
Finished: An initial directory structure has been created.
```

> 不谦虚地说，Sphinx除了用RST作为基础标记语言而不是用Markdown以外，思路与我基本一致啊。

## toctree

目前 reST 还没有专门的语法表示文件的相互关联或怎样将一份文档拆分成多个输出文件， Sphinx 使用自定义的指令在独立文件里添加这种关系或目录表格. 指令 `toctree` 是其核心元素.

> `toctree` 是 reStructuredText的 *directive* （指令）, 一种用途十分广泛的块标记. 定义了参数、选项及目录.
>
> *Arguments* 直接在双冒号后面给出指令的名字. 每个指令都有不定个数的参数.
>
> *Options* 在参数后以”字段列表”的形式给出. 如 `maxdepth` 是 `toctree` 指令的选项之一.
>
> *Content* 具体内容,在选项或参数的后面，隔开一个空行. 每个指令后面都跟着不同作用的内容.
>
> 共同的约定是 **内容与选项一般有相同的缩进** .



# Javadoc



