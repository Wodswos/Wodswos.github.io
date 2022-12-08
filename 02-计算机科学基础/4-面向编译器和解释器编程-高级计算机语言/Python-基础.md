# 基础中的基础

## 内置数据类型



### 字符串

字符串前：

```python
u'一些字符'
r'C:\Users\name\Desktop'
b'some string'
f'strign{variables}{expression}'
```

u 表示 unicode 格式编码

r 表示去除反斜杠的转义机制

b 表示 bytes 类型

f 表示在字符串内支持大括号内的python表达式



转义：

\r 表示将光标回退到开始位置。

# 内置函数和库

## 内置函数

`enumerate()`函数用于将一个可遍历的数据对象（如列表、字符串）组合为一个索引序列

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# output: [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# 每一个数据对象如 'Sprint' 被赋予了一个标号 (0) 并组合成一个元组。
for index, season in enumerate(seasons)
	print(index, season)
# 或者
for item in enumerate(seasons)
	print(item[0], item[1])
```





# 解释器[^1]



1. 完成模块的加载和链接
2. 将源代码翻译为**PyCodeObject**对象（这货就是字节码），并将其写入内存当中（方便CPU读取，起到加速程序运行的作用）
3. 从上述内存空间中读取指令并执行
4. 程序结束后，根据命令行调用情况（即运行程序的方式）决定是否将PyCodeObject写回硬盘当中（也就是直接复制到.pyc或.pyo文件中）
5. 之后若再次执行该脚本，则先检查本地是否有上述字节码文件。有则执行，否则重复上述步骤。[^1]





## `__pycache__`和“字节码”[^1]

* `.pyc`文件是由.py文件经过编译后生成的字节码文件，其**加载速度相对于之前的.py文件有所提高**，而且还可以**实现源码隐藏**，以及**一定程度上的反编译**。比如，Python3.3编译生成的.pyc文件，Python3.4就别想着去运行啦！
* `.pyo`文件也是**优化**（注意这两个字，便于后续的理解）编译后的程序（**相比于.pyc文件更小**），也可以**提高加载速度**。但对于嵌入式系统，它可将所需模块编译成.pyo文件以**减少容量**。



## 解释和编译





[^1]:Python什么情况下会生成pyc文件？ - 折木奉太郎的回答 - 知乎 https://www.zhihu.com/question/30296617/answer/112564303