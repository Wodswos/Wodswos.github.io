



# 社区管理：PEP

主要有以下几类的PEP，然后再根据PEP种类分配编号（有点类似http状态码的分配）

- [Meta-PEPs (PEPs about PEPs or Processes)](https://www.python.org/dev/peps/#meta-peps-peps-about-peps-or-processes)
- [Other Informational PEPs](https://www.python.org/dev/peps/#other-informational-peps)
- [Provisional PEPs (provisionally accepted; interface may still change)](https://www.python.org/dev/peps/#provisional-peps-provisionally-accepted-interface-may-still-change)
- [Accepted PEPs (accepted; may not be implemented yet)](https://www.python.org/dev/peps/#accepted-peps-accepted-may-not-be-implemented-yet)
- [Open PEPs (under consideration)](https://www.python.org/dev/peps/#open-peps-under-consideration)
- [Finished PEPs (done, with a stable interface)](https://www.python.org/dev/peps/#finished-peps-done-with-a-stable-interface)
- [Historical Meta-PEPs and Informational PEPs](https://www.python.org/dev/peps/#historical-meta-peps-and-informational-peps)
- [Deferred PEPs (postponed pending further research or updates)](https://www.python.org/dev/peps/#deferred-peps-postponed-pending-further-research-or-updates)
- [Abandoned, Withdrawn, and Rejected PEPs](https://www.python.org/dev/peps/#abandoned-withdrawn-and-rejected-peps)

当然，新的PEP还在不断提出，相信Python也会越来越好。



# 模块管理

> You may have heard about PyPI, `setup.py`, and `wheel` files. These are just a few of the tools Python’s ecosystem provides for distributing Python code to developers, which you can read about in [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/).

![Python’s recommended built-in library and tool packaging technologies.](C:/Users/Five/Desktop/note/img/py_pkg_tools_and_libs.png)

## 基本单元

模块是Python项目管理的基本单位

* 在python中，py文件=模块，即`something.py = module`
* 多个`.py`文件（多个模块）可以打包成一个package，带`__init__.py`文件
  * 若没有`__init__.py`文件，python会将此目录视为一个普通目录，而不是一个包
  * py文件=模块，`__init__.py`文件自然也是一个模块，模块名就是package的名称



### Module搜索路径

当你`import`一个模块时，Python会在`sys.path`变量所包含的路径中搜索该模块。

python在命令行打印sys.path，会有类似的以下几条基础路径

```
'', 
'E:\\Env\\Python\\python38.zip',  #
'E:\\Env\\Python\\DLLs', 
'E:\\Env\\Python\\lib', 
'E:\\Env\\Python', 
'C:\\Users\\UserName\\AppData\\Roaming\\Python\\Python38\\site-packages', 
'E:\\Env\\Python\\lib\\site-packages', 
'E:\\Env\\Python\\lib\\site-packages\\pip-20.2.3-py3.8.egg'
```

目录`.../Python/lib/site-packages`好像就是放各种`pip`来的库的。![image-20201108161157267](C:\Users\Five\Desktop\note\img\image-20201108161157267.png)



在命令行执行`python test.py`命令（`test.py`里写`import os `和`print(sys.path) `）

最终`sys.path`的结果会多一行，即会添加`test.py`文件所在的目录。

```
'C:\\Users\\Five\\Desktop'
```



在PyCharm IDE中打印`sys.path`的值，还会额外多几个路径（IDE好心，但有时候会办坏事）。

两条跟你当前的工作目录（执行`sys.path`的python文件所在的目录）有关，两条跟PyCharm有关：

```
'C:\\Users\\Five\\Desktop\\...\\the_dir_your_pyfile_located', 
'C:\\Users\\Five\\Desktop\\...\\package_location', 
'E:\\IDE\\JetBrains\\PyCharm\\plugins\\python\\helpers\\pycharm_display', 'E:\\IDE\\JetBrains\\PyCharm\\plugins\\python\\helpers\\pycharm_matplotlib_backend']
```



### 基本导入语法

执行`import`时，解释器会从`sys.path`中的路径搜索`module`。

```python
import numpy as np
myarray = np.ndarray()
```

此时导入的是numpy这个package下的`__init__.py`文件对应的模块。

## 调用np.ndarray的全过程

显然`Class ndarray`不是在模块`numpy/__init__.py`中定义的，那当我们使用`np.ndarray`的时候经历了怎样的调用关系呢。

在`numpy/__init__.py`模块中有如下导入

```python
from . import core
from .core import *
```

1. 第一句导入了模块`numpy/core/__init__.py`
2. 第二句导入了

在`_multiarray_umath`模块中有`ndarray`的定义。

```python
class ndarray(object):
    """
    ndarray(shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None)
    
        An array object represents a multidimensional, homogeneous array
        of fixed-size items.  An associated data-type object describes the
        format of each element in the array (its byte-order, how many bytes it
        occupies in memory, whether it is an integer, a floating point number,
        or something else, etc.)
    
        Arrays should be constructed using `array`, `zeros` or `empty` (refer
        to the See Also section below).  The parameters given here refer to
        a low-level method (`ndarray(...)`) for instantiating an array.
    
        For more information, refer to the `numpy` module and examine the
        methods and attributes of an array.
        """
    def any_subfunction_else():
        pass
```



### 导入具体的函数或类

```python
from numpy.core._multiarray_umath import ndarray
```



## 调用自己的模块

同目录下当然没有问题，但跨目录会报错`ModuleNotFoundError: No module named  xxx`



# 库管理

Python的流行离不开优秀的社区，海量卓越的第三方库被分享和使用。

那么该如何分享一个库呢，最简单的自然就是用源代码。

## Source Code

之前提到了Python会在`sys.path`变量所包含的路径中搜索模块，所以直接将源代码放到`sys.path`中的一个路径中，如`C:/.../Python/lib/site-packages`，解释器自然就能够在该路径找到找到该模块代码。



### 版本控制工具

> [pip](https://packaging.python.org/key_projects/#pip) can install from either [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-Source-Distribution-or-sdist) or [Wheels](https://packaging.python.org/glossary/#term-Wheel), but if both are present on PyPI, pip will prefer a compatible [wheel](https://packaging.python.org/glossary/#term-Wheel).

```bash
pip install ./downloads/SomeProject-1.0.4.tar.gz
```



### 用C++/C编写Python库





## PEP427和Wheel

> Egg is A [Built Distribution](https://packaging.python.org/glossary/#term-Built-Distribution) format introduced by [setuptools](https://packaging.python.org/key_projects/#setuptools), which is being replaced by [Wheel](https://packaging.python.org/glossary/#term-Wheel). For details, see [The Internal Structure of Python Eggs](https://setuptools.readthedocs.io/en/latest/deprecated/python_eggs.html) and [Python Eggs](http://peak.telecommunity.com/DevCenter/PythonEggs)
>
> Egg和esay_intall是Python曾经流行的标准和安装方式，目前基本已经被wheel + pip取代。
>
> 
>
> 《PEP 427 -- The Wheel Binary Package Format 1.0》
>
> A [Built Distribution](https://packaging.python.org/glossary/#term-Built-Distribution) format introduced by [**PEP 427**](https://www.python.org/dev/peps/pep-0427), which is intended to replace the [Egg](https://packaging.python.org/glossary/#term-Egg) format. Wheel is currently supported by [pip](https://packaging.python.org/key_projects/#pip).

下图是`numpy`部分轮子的截图。轮子命名规范通常为`{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`.

`python tag`中`cp`表示`CPython`，`ip`表示`IronPython`，`pp`表示`PyPy`，`jy`表示`Jython`。

![image-20201223201843225](C:\Users\Five\Desktop\note\img\image-20201223201843225.png)



直接用“轮子”命名，其目的和意义也是够直白了。

如果在PyPI上同时有匹配的Source Code和Wheel，pip会倾向于Wheel优先。

> 跟Java的jar包类似，都是zip类型文件的再开发和规范化。
>
> A wheel is a ZIP-format archive with a specially formatted file name and the `.whl` extension. It contains a single distribution nearly as it would be installed according to [PEP 376](https://www.python.org/dev/peps/pep-0376) with a particular installation scheme. Although a specialized installer is recommended, a wheel file may be installed by simply unpacking into site-packages with the standard 'unzip' tool while preserving enough information to spread its contents out onto their final paths at any later time.

> 个人猜测：文件夹作为一种特殊的文件，往往跟文件系统挂钩，即同样一个目录文件，在不同文件系统下是不一样的。
>
> 为了解决这个问题，需要引入一种兼容的格式——往往是zip。（解压软件会承担文件系统的识别和适配工作）
>
> 不仅仅是包的发布如此，HTTP下载的时候普遍会用这样的方式避免文件系统的差异。

> 《PEP 376 Database of Installed Python Distributions》
>
> Combined with [PEP 345](https://www.python.org/dev/peps/pep-0345), the current proposal supersedes [PEP 262](https://www.python.org/dev/peps/pep-0262)(Create an installation database).
>
> Note: the implementation plan didn't go as expected, so it should be considered informative only for this PEP.

### wheel标准和示例解剖

从镜像站下载一个numpy的`.whl`文件，可以用解压软件打开（如果软件不能自动识别，可以将wheel文件后缀改成zip），可以得到三个文件夹。

> 在wheel的实际安装过程中第一步也是解压。





#### `package-version.data`



#### `package-version.dist-info`



![image-20201223202307741](C:\Users\Five\Desktop\note\img\image-20201223202307741.png)

其中dist-info（Distribution-information）文件夹中有如下内容

![image-20201223202359195](C:\Users\Five\Desktop\note\img\image-20201223202359195.png)

用记事本打开WHEEL文件（内容不多）

![image-20201223203927109](C:\Users\Five\Desktop\note\img\image-20201223203927109.png)

numpy文件夹（也可能是package_name.data文件夹）中的内容就和numpy开源在github上的仓库（中的numpy子文件夹）差不多一致了。

![image-20201223202613729](C:\Users\Five\Desktop\note\img\image-20201223202613729.png)



#### `package`



### wheel安装过程（pip）

- Unpack.
  1. Parse `distribution-1.0.dist-info/WHEEL`.
  2. Check that installer is compatible with Wheel-Version. Warn if minor version is greater, abort if major version is greater.
  3. If Root-Is-Purelib == 'true', unpack archive into purelib (site-packages).
  4. Else unpack archive into platlib (site-packages).
- Spread.
  1. Unpacked archive includes `distribution-1.0.dist-info/` and (if there is data) `distribution-1.0.data/`.
  2. Move each subtree of `distribution-1.0.data/` onto its destination path. Each subdirectory of `distribution-1.0.data/` is a key into a dict of destination directories, such as `distribution-1.0.data/(purelib|platlib|headers|scripts|data)`. The initially supported paths are taken from `distutils.command.install`.
  3. If applicable, update scripts starting with `#!python` to point to the correct interpreter.
  4. Update `distribution-1.0.dist-info/RECORD` with the installed paths.
  5. Remove empty `distribution-1.0.data` directory.
  6. Compile any installed .py to .pyc. (Uninstallers should be smart enough to remove .pyc even if it is not mentioned in RECORD.)

> 虽然实际中都是直接`pip`，就会自动完成如上过程，但能将对`pip`的从黑盒变成白盒，自然也是极好的。



## pip和PyPI

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

用如上所示的pip命令去安装一个社区的库，简洁快速，不得不说……是一种非常爽的体验。

从pypandoc这种冷门的AutoOffice工具到Tensorflow这种火热的机器学习库，python的库应有尽有。



> The Python Package Index (PyPI) is a repository of software for the Python programming language.

> 加载所有的PyPI的项目目录用了好久，真的是巨长的一个列表。
>
> 而每个成熟的项目（如Tensorflow）打开之后又会有巨长的各种version轮子列表。
>
> 下图是Tensorflow的极小一部分轮子（清华镜像站）：
>
> ![image-20201223174029303](C:\Users\Five\Desktop\note\img\image-20201223174029303.png)

```python
# 查看自己的Python所支持的wheel包类型。
from pip import pep425tags
print(pep425tags.get_supported())
```

除了PyPI之外，也可以从其他的Indexs下载（当然一般用不到，但也足够说明Python的自由和灵活）。

```bash
pip install --index-url http://my.package.repo/simple/ SomeProject
pip install --extra-index-url http://my.package.repo/simple SomeProject
```

自然也可以使用镜像

```bash
# 单次指定镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
# 多次使用，设为默认（pip版本>=10.0.0）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



> [pip](https://packaging.python.org/key_projects/#pip) can install from either [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-Source-Distribution-or-sdist) or [Wheels](https://packaging.python.org/glossary/#term-Wheel), but if both are present on PyPI, pip will prefer a compatible [wheel](https://packaging.python.org/glossary/#term-Wheel).

## 制作一个自己的轮子[^1]

> 基本上是复制官方文档。

新建一个package，如`hello_pkg`

![image-20201223214747240](C:\Users\Five\Desktop\note\img\image-20201223214747240.png)

然后需要一堆文件

```
packaging_tutorial
├── LICENSE
├── README.md
├── hello_pkg
│   └── __init__.py
├── setup.py
└── tests
```

> tests和README.md都暂且为空，无关紧要

`setup.py`内容如下

```python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

> 参数的详细解释参加官网：
>
> https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py

```bash
python3 setup.py sdist bdist_wheel
```

### 打包工具和`setup.py`[^10]





* `disutils`
  * 万物起源，Python的标准库，官方开发的分发打包工具
* `setuptools`
  * Egg 格式就是由 setuptools 在 2004 年引入的
* `distutils`
* `distutiles2`
  * 试图尝试充分利用distutils，detuptools 和 distribute 并成为 Python 标准库中的标准工具。
  * 但该计划并没有达到预期的目的，且已经是一个废弃的项目。







### 上传到PyPI-twine

为了练习，官方特地准备了个TestPyPI，这里上传的内容不会影响主索引库，但步骤和主索引库的上传完全相同。

```bash
# 如果是上传到主索引，需将testPyPI替换成PyPI
python3 -m twine upload --repository testpypi dist/*

# 可以使用用户名登录，也可以使用API Token
# Enter your username:__token__
# Enter your password:生成的API Token复制粘贴到这里即可
```

上传成功后你就可以获取并安装自己的库了（当然要指定索引为TestPyPI）。

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
```



## 其他

Python支持从Version Control System（即Git、SVN等）下载并安装packages。

```bash
pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
pip install -e hg+https://hg.repo/some_pkg#egg=SomeProject                # from mercurial
pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch
```



# 环境管理

![image-20210207131959602](C:\Users\Five\Desktop\note\img\image-20210207131959602.png)

如上图所示，Python蓬勃发展，在变得越来越强大的同时也越来越庞杂、重量化。

当情况更加复杂，比如需要用Python处理多个不同类型（可视化、分布式、web、机器学习等）的项目时，而我们又不想让这些项目共用一个Python庞大沉重、依赖复杂的环境时，能不能创建并管理多个环境？又该如何管理多个环境？

virtualenv或者conda是比较成熟的解决方案。





## virtualenv

`vitualenv`是用python写的，反过来用于python的环境管理。



## conda

> conda因Python而生，但其能力不止于此：
>
> Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.	

conda $\approx$ pip + virtualenv



### Anaconda

> [Conda](https://conda.io/en/latest) is an open source package management system and environment management system included in Anaconda and Miniconda. Learn [how to get started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).[^6]

Anaconda是Python的一个发行版——也可以说是Python和Conda的发行版。

Anaconda包括了基本的Python解释器、Conda和其他一些常用的库（如Numpy、sk-learn）。

> 发行版（distro），最著名的例子自然是Linux内核和Linux发行版。Anaconda和Python的关系也类似CentOS和Linux内核的关系

> 更多Anaconda的信息可参考以下链接
>
> https://www.anaconda.com/library
>
> https://www.anaconda.com/blog
>
> https://docs.anaconda.com/anaconda/user-guide/

### miniconda





### conda vs pip+virtualenv[^7][^8][^9]

pip是用来安装python包的，安装的是python wheel或者源代码的包。从源码安装的时候需要有编译器的支持，pip也不会去支持python语言之外的依赖项。

conda是用来安装conda package，虽然大部分conda包是python的，但它支持了不少非python语言写的依赖项，比如mkl cuda这种c c++写的包。

> Conda的NumPy、SciPy直接使用Intel MKL，对Intel的CPU支持更好。
>
> https://www.anaconda.com/blog/scikit-learn-speed-up-with-intel-and-anaconda



# 项目打包和导出

![The simplified gamut of technologies used to package Python applications.](C:/Users/Five/Desktop/note/img/py_pkg_applications.png)



https://mp.weixin.qq.com/s/rNcrLbPSkBKfw3VNr9XYnA







# 一趟完整的开发流程







[^1]:https://www.cnblogs.com/tkqasn/p/6001134.html
[^2]:https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files
[^3]:http://www.mxm.dk/2008/02/python-eggs-simple-introduction.html
[^4]:Python eggs - 简介 - 「已注销」的文章 - 知乎 https://zhuanlan.zhihu.com/p/25020501
[^5]:https://mp.weixin.qq.com/s/rNcrLbPSkBKfw3VNr9XYnA
[^6]:https://docs.anaconda.com/anaconda/user-guide
[^7]:请问大神们，pip install 和conda install有什么区别吗？ - 马索萌的回答 - 知乎 https://www.zhihu.com/question/395145313/answer/1230725052
[^8]:请问大神们，pip install 和conda install有什么区别吗？ - PP鲁的回答 - 知乎 https://www.zhihu.com/question/395145313/answer/1257660174
[^9]:https://www.anaconda.com/blog/understanding-conda-and-pip
[^10]:https://mp.weixin.qq.com/s/rNcrLbPSkBKfw3VNr9XYnA