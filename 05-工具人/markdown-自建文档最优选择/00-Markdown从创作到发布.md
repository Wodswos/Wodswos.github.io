# 本地写作-Typora

这个不多说了



个人习惯还是在本地先写。



----

2020年10月4日补充：

**我草泥马的，灯下黑啊**

Typora本身就支持导出HTML、PDF多种格式导出，数学公式渲染好，排版也整齐……

我他妈还浪费那么多时间在外面找那么多妖艳贱货，我对不起你啊Typora！

> 但Typora导出……要手动一个也给去export……数量一多还要重复导出就有点蠢了。

# Pandoc

### 基础使用

> 目前这些基础使用实验我基本失败了……主要还是公式渲染和排版问题吧

* 添加CSS

```bash
pandoc in.md -c style.css out.html
```

Pandoc默认目录是`C:\Users\USERNAME\AppData\Roaming\pandoc` ，只需要将这个style.css文件放入到这个目录下，那么在任意目录使用pandoc时，都能自动读取到这个文件



* 附带CSS和图片等信息生成独立HTML

```bash
pandoc -s -H style.css  in.md -o out.html
```



```bash
pandoc -s --self-contained -c style.css in.md -o out.html
```

* 导出PDF

指定TeX引擎

```bash
pandoc in.md -o out.pdf --latex-engine=xelatex
```



### Extras

#### GUI

#### CLI Wrappers

# Manubot! YES!

完美符合我预期的workflow，观念也很吻合







# 从源文件到个人网站发布一条龙

1. Copy Source to Post，在Post文件夹的基础上进行处理

   >建立一个post文件夹，作为本地文件和云端发布的中间形态，在post里将本地版本调整为云端发布版本，修改错了也不会影响最原始版本，大不了删了再复制一份。
   >
   >有点类似git中间仓库的思想

2. 更改图片路径，从本地切换到阿里云oss存储服务

   刚开始是手动匹配替换……显然那样太低效愚蠢了，所以写了Python代码进行自动化处理

   ```python
   # img_path_convert
   import os
   
   dir_list = [os.getcwd()]
   markdown_list = []
   
   # 本代码在复杂度上优化的并不好，不过我觉得毕竟就小规模处理，所以我也不太缺那点优化，逻辑简单是优先级最高的事
   # 先递归遍历当前文件夹，找到所有的markdown文件的绝对路径
   while dir_list:
       current_work_dir = dir_list[0]
       dir_list.pop(0)
   
       for sub_item in os.listdir(current_work_dir):
           absolute_item_path = current_work_dir + "\\" + sub_item
           if os.path.isdir(absolute_item_path):
               print("Find and add a subdir: " + absolute_item_path)
               dir_list.append(absolute_item_path)
           else:
               if sub_item.endswith(".md"):
                   markdown_list.append(current_work_dir + "\\" + sub_item)
   
   # 逐个处理markdown文件
   print(markdown_list)
   for item in markdown_list:
       with open(item, 'r+',encoding='utf8') as f:
           # 读取文件并进行路径替换
           text = f.read()
           print(text)
           text = text.replace("your local path in Linux Syntax", "your alioss path")
           text = text.replace("your local path in Windows Syntax", "your alioss path")
           # 清空文件并重写
           f.seek(0)
           f.truncate()
           f.write(text)
           print("Complete the replace task of file " + item)
   
   ```

   

3. 目前还是手动用typora去打开每一个markdown文件并导出html文件……我知道很愚蠢，待我有空了去学学electron，看看Typora到底是怎么运作的具体

4. 然后就可以上传到云服务器了。



## 其他小的Improvement

### 添加文章网址的icon

1. 添加favicon.ico到index.html所在文件夹
2. 在index.html文件\<head>下增加如下标签

```html
\<link rel="shortcut icon" href="favicon.ico">
```



### 自动为README文件追加索引

手写索引很麻烦，而且文件名改了索引还要手动修改，那简直是噩梦。

所以最原始版本不添加索引，在post到网站的时候统一用Python在README文件末尾追加索引超链接

（此代码仅索引一层，不递归索引）

```python
import os
import sys

README_list = []
dir_list = [os.getcwd()]

# 递归搜索找到有所的README.md文件
while dir_list:
    current_work_dir = dir_list[0]
    dir_list.pop(0)

    for sub_item in os.listdir(current_work_dir):
        absolute_item_path = current_work_dir + "/" + sub_item
        if os.path.isdir(absolute_item_path):
            # print("Find and add a subdir: " + absolute_item_path)
            dir_list.append(absolute_item_path)
        else:
            if sub_item == "README.md":
                README_list.append(current_work_dir + "/" + sub_item)

print("find these README file: ", README_list)


def get_text(dir, item):
    if os.path.isdir(dir + item):
        return '[' + item + '](' + item + '/index.html)'
    elif item.endswith(".md"):
        item = item.strip(".md")
        return '[' + item + '](' + item + '.html)'


def get_index_info(index_dir):
    index_list = []
    for index_item in os.listdir(index_dir):
        if index_item == "README.md":
            pass
        else:
            text = get_text(index_dir, index_item)
            if text:
                index_list.append(text)
    return index_list


print(len(README_list))
for README_file_absolute_path in README_list:
    index_info = get_index_info(README_file_absolute_path.strip("README.md"))
    # print(index_info)
    with open(README_file_absolute_path, 'a+',encoding='utf8') as f:
        f.write("\n")
        for item in index_info:
            f.write('* '+ item + '\n')

    print("-------auto append the index for README file: " + README_file_absolute_path+"---------")

```



# 互联网论坛/平台发布

### 公式支持

都很差，不如Typora的渲染。

### 多平台发布工具

Openwrite

个人对紧耦合一直很恐惧……这也是为啥用Markdown而不用特定平台（知乎啊、博客园啊、CSDN啊、简书啊）的原因。



# 图片云存储-阿里OSS

给自己的本地图片存放路径也定个规范，比如所有图片统一存放在某一目录下，按章节-本章节第N张编号。

> 后来发现不用编号也很好，照片不重名就行，编号完全是自找没事



> 同时不得不说，Windows默认路径用反斜杠确实有点nt。

最后发布的时候统一把所有的所有picture的路径（已经定了规范了，就很方便批量查找和替换）替换为阿里云OSS服务的URL



### 阿里云OSS介绍

[阿里云对象存储服务官方文档](https://help.aliyun.com/product/31815.html)

![image-20201003145947185](C:\Users\Five\Desktop\book\img\00-01.png)



### PicGo

![image-20201003160022102](C:\Users\Five\Desktop\book\img\00-02.png)



……其实吧，设完之后发现自己的流程中不太需要PicGo，自己手动批量上传到阿里云也很方便……，毕竟我不是一开始就在文章里就用阿里云oss的URI，而是先用本地路径，最后发布的时候批量替换的。

所以PicGo的功能对我而言收益不大。



# 数学公式渲染

> Typora supports rendering normal mathematics using Tex/LaTeX syntax. The rendering process is processed by [MathJax](https://www.mathjax.org/).

而且pandoc的默认形式好像只支持typora内的行内公式，而不支持独立模式。同时\$符号后不能跟数字和空格……有点离谱。

而且pandoc渲染的公式和Typora自带的渲染效果……很不一样，总之原生的pandoc着实没有Typora效果好。

官方文档如下：

> Anything between two `$` characters will be treated as TeX math. The opening `$` must have a non-space character immediately to its right, while the closing `$` must have a non-space character immediately to its left, and must not be followed immediately by a digit. Thus, `$20,000 and $30,000` won’t parse as math.

但用Typora难道要手动一个个导出嘛，那也太蠢了。



## MathJax

```html
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
```

```html
<!DOCTYPE html>
<html>
<head>
<title>Jartto's MathJax Demo </title>
<script type="text/javascript" async
  src="https://example.com/mathjax/MathJax.js?config=AM_CHTML"></script>
</head>
<body>

<p>When `a != 0`, there are two solutions to `ax^2 + bx + c = 0` and
they are</p>
<p style="text-align:center">
  `x = (-b +- sqrt(b^2-4ac))/(2a) .`
</p>

</body>
</html>
```







## KaTeX