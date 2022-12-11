虽然很早就对BeautifulSoup有所耳闻，但介于个人对爬虫的兴趣……并不算高涨，甚至为了避免自己信马由缰，学得太杂，一度把爬虫拉入黑名单，所以一直没入坑。

> 希望BeautifulSoup能达到我预期的批量修改html的效果。

文档基本是以目的（批量修改我个人博客的html）为导向的，所以比较信马由缰，内容未必有太多参考价值。

# 概述

解析得到`soup`对象

```python
# 解析文本
soup = BeautifulSoup(html_text,'html.parser')
# 解析文件(传入文件句柄)
soup = BeautifulSoup(open('filename.html'),'html.parser')
```



## 解析器

| 解析器           | 使用方法                                                     | 优势                                                         | 劣势                                          |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------- |
| Python标准库     | `BeautifulSoup(markup, "html.parser")`                       | Python的内置标准库<br />执行速度适中<br />文档容错能力强     | Python 2.7.3 or 3.2.2前的版本中文档容错能力差 |
| lxml HTML 解析器 | `BeautifulSoup(markup, "lxml")`                              | 速度快<br />文档容错能力强                                   | 需要安装C语言库                               |
| lxml XML 解析器  | `BeautifulSoup(markup, ["lxml-xml"])``BeautifulSoup(markup, "xml")` | 速度快<br />唯一支持XML的解析器                              | 需要安装C语言库                               |
| html5lib         | `BeautifulSoup(markup, "html5lib")`                          | 最好的容错性<br />以浏览器的方式解析文档<br />生成HTML5格式的文档 | 速度慢<br />不依赖外部扩展                    |



## 对象种类详解

* `Tag`
* `NavigableString`
* `BeautifulSoup`
* `Comment`



### Tag

* 多值属性

最典型的是`class`属性，对于多值属性，BeautifulSoup返回的是一个列表。



### NavigableString

字符串常被包含在`tag`内。Beautiful Soup用 `NavigableString` 类来包装`tag`中的字符串。

```python
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
```



### BeautifulSoup

大部分情况下可以把`BeautifulSoup`对象作为一种特殊的`tag`对待。





## 文档树操作

### 获取标签

最快捷的方法是用点标记，如获取`body`中第一个`b`标签代码如下：

```python
soup.body.b
# <b>The Dormouse's story</b>
```

`find_all()`获取全部的标签

```python
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```



#### 配合re模块使用

查找`h1-h6`的所有标题标签，就可以通过配合re模块实现

```python
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("inpage_test.html"),'lxml')
print(soup.find_all(re.compile('^h\d$')))
# 可能会误匹配h7,h8啥的，但这样写好像比较优雅
```

这里soup部分没啥好说的，倒是re部分可以温习温习：

| 模式        | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| ^           | 匹配字符串的开头                                             |
| $           | 匹配字符串的末尾。                                           |
| .           | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。 |
| [...]       | 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'          |
| [^...]      | 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。             |
| re*         | 匹配0个或多个的表达式。                                      |
| re+         | 匹配1个或多个的表达式。                                      |
| re?         | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式         |
| re{ n}      | 精确匹配 n 个前面表达式。例如， **o{2}** 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。 |
| re{ n,}     | 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。 |
| re{ n, m}   | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式         |
| a\| b       | 匹配a或b                                                     |
| (re)        | 对正则表达式分组并记住匹配的文本                             |
| (?imx)      | 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。 |
| (?-imx)     | 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。     |
| (?: re)     | 类似 (...), 但是不表示一个组                                 |
| (?imx: re)  | 在括号中使用i, m, 或 x 可选标志                              |
| (?-imx: re) | 在括号中不使用i, m, 或 x 可选标志                            |
| (?#...)     | 注释.                                                        |
| (?= re)     | 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。 |
| (?! re)     | 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功 |
| (?> re)     | 匹配的独立模式，省去回溯。                                   |
| \w          | 匹配字母数字及下划线                                         |
| \W          | 匹配非字母数字及下划线                                       |
| \s          | 匹配任意空白字符，等价于 **[ \t\n\r\f]**。                   |
| \S          | 匹配任意非空字符                                             |
| \d          | 匹配任意数字，等价于 [0-9].                                  |
| \D          | 匹配任意非数字                                               |
| \A          | 匹配字符串开始                                               |
| \Z          | 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。 |
| \z          | 匹配字符串结束                                               |
| \G          | 匹配最后匹配完成的位置。                                     |
| \b          | 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。 |
| \B          | 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。 |
| \n, \t, 等. | 匹配一个换行符。匹配一个制表符。等                           |
| \1...\9     | 匹配第n个分组的内容。                                        |
| \10         | 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。 |

### 新建标签

创建一个`tag`最好的方法是调用工厂方法`BeautifulSoup.new_tag()`

```python
soup = BeautifulSoup("<b></b>")
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
original_tag
# <b><a href="http://www.example.com"></a></b>

new_tag.string = "Link text."
original_tag
# <b><a href="http://www.example.com">Link text.</a></b>
```

