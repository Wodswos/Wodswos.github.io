# Python内置库

## argparse

 Parser for command-line options, arguments and sub-commands

## 爬虫-Scrapy（A turtorial）

一般来说，基本的爬虫流程为：



![](C:/Users/Five/Desktop/note/img/20210601165055708.png)



基于此，scrapy（[Scrapy 2.6 documentation — Scrapy 2.6.1 documentation](https://docs.scrapy.org/en/latest/)）的架构为：

![](C:/Users/Five/Desktop/note/img/13139608-89968f7679956532.webp)



![](C:/Users/Five/Desktop/note/img/13139608-bd4591105104b29e.webp)

### 创建一个Spider



```bash
scarpy startproject <project_name>
```



### Scrapy文件目录结构和总体架构的对应关系



![](C:/Users/Five/Desktop/note/img/20210601200508268.png)



#### settings.py



### 创建爬虫文件



可以手动在`spiders`目录下创建python文件，也可以用scrapy的命令创建：

```
cd 
scrapy genspider <file_name><domain_name>
```





### 定义数据容器





### 编写爬虫Spider





### 运行爬虫



```
scrapy crawl spider_name -o outputfile.jl
```



# 自动化工具

## Fabric

* 一个让你通过命令行执行无参数Python函数的工具；
* 一个让通过 SSH 执行 Shell 命令更加容易、更符合Python风格的命令库（建立于一个更低层次的库）。



## Pandas

如何最简单、通俗地理解Python的pandas库？ - 朱卫军的回答 - 知乎 https://www.zhihu.com/question/433408227/answer/1978803602

官网十分钟教程： https://pandas.pydata.org/docs/user_guide/10min.html

官网cookbook： https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook




![](C:/Users/Five/Desktop/note/img/fd1d6789d47c279547870b0b5f294eaa.png)

## Sphinx

https://www.sphinx-doc.org/en/master/

# 可视化





## 关于图片处理

### PIL



### scikit-image

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-image
```

```python
import skimage
```

### opencv



## pyecharts

https://gallery.pyecharts.org/#/README





# 科学计算






# 机器学习





# 其他

## tqdm

`tqdm`是一个快速的，易扩展的进度条提示模块。

官网：https://tqdm.github.io/

> `tqdm` *derives from the Arabic word* *taqaddum* *(تقدّم) which can mean “progress,” and is an abbreviation for “I love you so much” in Spanish (**te quiero demasiado**).*

```python
from tqdm import trange
import time

from tqdm import trange, tqdm
for i in trange(10):
    time.sleep(0.5)
```

或者

```python
from tqdm import tqdm

pbar = tqdm(total=100) # 也可以用with语句，如with tqdm(total=100) as pbar
for i in range(100):
    time.sleep(0.1)
    pbar.update(1)
```

