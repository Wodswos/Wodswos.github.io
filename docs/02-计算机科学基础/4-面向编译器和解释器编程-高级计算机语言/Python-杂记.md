# StackOverflow Python问题答案vote数Top10

> 在Stack Overflow通过如下筛选条件得到的十大高票答案极其问题：
>
> ![image-20210202132345509](C:\Users\Five\Desktop\note\img\image-20210202132345509.png)
>
> 此处以答案的内容为基础，会有适当补充。

## 如何理解Yield关键字





## 如何理解`if __name__=="__main__:"`

原问题`What does if __name__=="__main__": do`





## 如何理解三元运算符







## 如何理解metaclass



## 如何判断一个文件是否存在（不用异常捕获）





## 如何一个表达式合并两个字典







## 如何用Python调用外部命令





## 如何安全的创建一个多层文件夹





## 循环中如何访问下标

`enumerate`嘛，这个倒是基础。



## staticmethod和classmethod的区别







# Python日期和时间处理

## 内置模块time

time模块中主要有三种时间表示格式：timestamp, struct_time, format time.

![](C:/Users/Five/Desktop/note/img/996085-20161026171443546-488752980.png)

### timestamp

时间最原始、最通用的格式。

> 很多编程语言起源于UNIX系统，而UNIX系统认为1970年1月1日0点是时间纪元，所以常说的UNIX时间戳是以1970年1月1日0点为计时起点时间的（格林尼治时间）。
>
> 格林尼治时间1970年1月1日0点是北京时间1970年1月1日8点。（东十二区时间最早）

```python
import time
timestamp_example = time.time()
```

```python
# 从struct_time转换而来
timestample = time.mktime(time.localtime())
```



### struct_time

九元组`(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)`。

```
tm_wday（weekday）             0 - 6（0表示周日）
tm_isdst（是否是夏令时）        默认为-1
```

```python
# 直接获取struct_time格式
import time
struct_time_example = time.localtime()
print(truct_time_example)

# [output]: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=21, tm_hour=21, tm_min=51, tm_sec=15, tm_wday=0, tm_yday=356, tm_isdst=0)
```

```python
# 通过timestamp转换而来
import time
timestamp = time.time()
struct_time_example = time.gmtime(timestamp)
# 或者struct_time_example = time.localtime(timestamp)
print(truct_time_example)

# [output]: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=21, tm_hour=21, tm_min=51, tm_sec=15, tm_wday=0, tm_yday=356, tm_isdst=0)
```

`struct_time`的九元组是`readonly`属性，不能直接修改。





### format time

更强的可读性，用于交互，但不适合用于机器处理。

```python
print(time.strftime('%Y 一堆自定义内容 %m %d'), struct_time_example)
print(time.strftime('%Y-%m-%d  %H:%M:%S'), struct_time_example)
```

| **格式** | **含义**                                                     |
| -------- | ------------------------------------------------------------ |
| %a       | 本地（locale）简化星期名称                                   |
| %A       | 本地完整星期名称                                             |
| %b       | 本地简化月份名称                                             |
| %B       | 本地完整月份名称                                             |
| %c       | 本地相应的日期和时间表示                                     |
| %d       | 一个月中的第几天（01 - 31）                                  |
| %H       | 一天中的第几个小时（24小时制，00 - 23）                      |
| %I       | 第几个小时（12小时制，01 - 12）                              |
| %j       | 一年中的第几天（001 - 366）                                  |
| %m       | 月份（01 - 12）                                              |
| %M       | 分钟数（00 - 59）                                            |
| %p       | 本地am或者pm的相应符                                         |
| %S       | 秒（01 - 61）                                                |
| %U       | 一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 |
| %w       | 一个星期中的第几天（0 - 6，0是星期天）                       |
| %W       | 和%U基本相同，不同的是%W以星期一为一个星期的开始。           |
| %x       | 本地相应日期                                                 |
| %X       | 本地相应时间                                                 |
| %y       | 去掉世纪的年份（00 - 99）                                    |
| %Y       | 完整的年份                                                   |
| %Z       | 时区的名字（如果不存在为空字符）                             |
| %%       | ‘%’字符（和用`/`作转义异曲同工）                             |

## 内置模块datetime

`datetime`重新封装了`time`模块

主要有`time`、`date`、`datetime`、`timedelta`、`tzinfo`等类。



# Python黑魔法[^1]



# Python踩坑

## 文件读写

没错，就这么基础的操作，我还是踩坑了。

| 文件模式 | 备注                                                         |
| -------- | ------------------------------------------------------------ |
| r        | 只读打开，文件必须存在                                       |
| r+       | 可读写打开，文件必须存在                                     |
| w        | 只写打开，若存在文件清零，不存在则建立                       |
| w+       | 可读写打开，若存在文件清零，不存在则建立                     |
| a        | **只写打开**。不存在会新建，**附加方式**写：以原文件尾作为新起始头，即原文件内容会保留 |
| a+       | 可读写打开。附加方式写                                       |

> 在`a`和`a+`中，虽然`f.seek(0)`好像还是可以将光标移动到0（用`f.tell()`显示是在0了，`a+`的读操作也确实从0开始了），不过一旦`f.write()`，光标会回到文件末尾。

> 我踩坑在w+，我tm以为w+只是相比于r+多了一个文件不存在时创建文件，大部分文档也的确是这么写的。
>
> 结果啊，还有清空文件，所有 w 模式都是清空文件。我当时百思不得其解。
>
> （TM幸好机智如我备份了，不然直接原地爆炸）

## Python2和Python3

* Python2和Python3的除法不一样。Python2中根据操作数判断，Python3使用`/`和`//`两种不同的操作符。





[^1]:https://magic.iswbm.com/
