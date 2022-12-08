GNU（GNU's Not Unix）是一个自由的操作系统和**软件计划**，其软件内容完全以GPL许可证方式发布。

> GPL许可证开源的代码，他人经过修改后得到新代码也得继续沿用GPL许可证，即继续开源。

The GNU includes the `EMACS` editor, `GCC` compiler, `GDB` debugger, assembler, linker, utilities for manipulating binaries, and other components. 

几乎包含一个操作系统所有组件，唯独内核由Linux作为一个独立的project发展。

> GPL，General Public License，通用公共许可证
>
> 大多数软件许可证决意剥夺你共享和修改软件的自由。相比之下，GNU通用公共许可证试图保证你共享和修改软件的自由。——保证自由软件对所有用户是自由的。
>
> GPL适用于大多数[自由软件基金会](https://baike.baidu.com/item/自由软件基金会)的软件，以及由使用这些软件而承担义务的作者所开发的软件。（自由软件基金会的其他一些软件受GNU库通用许可证的保护）。你也可以将它用到你的程序中。当我们谈到自由软件（free software）时，我们指的是自由而不是价格（"free" as in "free speech," not "free beer"）。

GNU/Linux命名争议

> 自由软件基金会的创立者，理查德·斯托曼，以及其支持者，提出GNU/Linux的名称，希望用来作为Linux操作系统的正式名称。
>
> 在发展过程中Linux和GNU早已从事实上彼此促进，名义上独立发展。



# GCC

GCC，GNU Compiler Collection，GNU编译套件。

```
 gcc -o hello hello.c
```

然后这一行命令会执行如下过程1。

> gcc、g++、cpp 都叫做 compiler driver 。这些都不负责编译代码，只负责调用真正的编译器（compiler proper）。gcc 这个项目中，真正负责编译 C 代码的程序叫做 cc1，负责编译 C++ 代码的程序叫做 cc1plus 5

![image-20201206144004646](file://C:\Users\Five\Desktop\note\img\image-20201206144004646.png?lastModify=1631706564)

* 关于链接Linker
  * 以printf函数为例
  * 需要编译器提供（标准C库）printf.o，并合并到原文件，称为链接。

## 命令行参数

* `-x`，显式指定要编译的语言，指定后会忽略文件的后缀名，按指定的来
  * `-x none`表示关闭显式指定，使用场景：同时编译多个文件，前面的文件需要显式指定，而之后的文件根据后缀名判断
* `-E`，只做预处理，不生成文件，如需保存到文件则自己重定向输出
* `-S`，做预处理和编译，不汇编和连接，目标文件为汇编代码
* `-c`，做预处理、编译、汇编，不链接，目标文件为`obj`
* `-o`，指定编译产物的文件名
  * 大写的O，一般是与优化有关的参数
* `-ansi`，关闭GNU C中与ANSI C不兼容的特性
* `-w`，不生成任何警告信息
* `-Wall`，生成所有的警告信息

还有一些不常用的`-Dmacro`定义宏、`-UMACRO`取消宏的定义、`-include file`类似代码中的`#include<file>`、`-static`禁止使用共享链接等。

# make和Makefile[^2][^3]

> 代码变成可执行文件，叫做[编译](http://www.ruanyifeng.com/blog/2014/11/compiler.html)（compile）；
>
> 先编译这个，还是先编译那个（即编译的安排），叫做[构建](http://en.wikipedia.org/wiki/Software_build)（build）。
>
> GNU `make` conforms to section 6.2 of IEEE Standard 1003.2-1992 (POSIX.2).3

当项目是一个很大的工程时，仅仅用gcc去逐个编译耗时耗力，而且容易出错，所以make工具应运而生。

make工具是一个简化编译工作的程序。You must write a file called the `Makefile` that describes the relationships among files in your program and provides commands for updating each file.

```
 edit : main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
         cc -o edit main.o kbd.o command.o display.o \
                    insert.o search.o files.o utils.o
 
 main.o : main.c defs.h
         cc -c main.c
 kbd.o : kbd.c defs.h command.h
         cc -c kbd.c
 command.o : command.c defs.h command.h
         cc -c command.c
 display.o : display.c defs.h buffer.h
         cc -c display.c
 insert.o : insert.c defs.h buffer.h
         cc -c insert.c
 search.o : search.c defs.h buffer.h
         cc -c search.c
 files.o : files.c defs.h buffer.h command.h
         cc -c files.c
 utils.o : utils.c defs.h
         cc -c utils.c
 clean :
         rm edit main.o kbd.o command.o display.o \
            insert.o search.o files.o utils.o
```

## Rule、Target、Recipe

* 某种程度上Rule可以类比为函数

```
 targets : [prerequisites]
 <tab> [recipe]
 
 # 或者可以通过';'表示结束prerequistites部分
 targets : [prerequisites] ; [recipe]
```

* Target类似于函数名
  * 当然Target也是Rule执行后生成的目标文件名（如果有生成）
  * 如果Make命令运行时没有指定Target，默认会执行Makefile文件的第一个Target。
* prerequisites类似于函数参数
  * 只要有一个prerequisites的last-modified的时间戳比目标last-modified的时间戳新，“目标”就需要重新构建
  * prerequisites有normal和order-only两种类型
    * 通过管道符指明order-only类型
    * oreder-only类型的prerequisites时间戳更新不会rebuild
    * 同时声明normal和order-only时，normal优先
* recipe则类似于函数的具体内容



### Special Targets

Certain names have special meanings if they appear as targets.

`.PHONY`、`.SUFFIXES`、`.DEFAULT`、`.PRECIOUS`、`.INTERMEDIATE`、`.SECONDARY`、`.POSIX`等

* `.PHONY`用于声明Phony Target
  * 即`.PHONY`这个Target的Prerequisites会被视为伪目标



### Phony Target

A phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request.

There are two reasons to use a phony target: to avoid a conflict with a file of the same name, and to improve performance.4

```
 .PHONY: clean
 clean:
     rm *.o temp
```

如果不用Phony Target，且当前文件夹中存在一个`clean`文件，那么该条rule不会被执行。（因为没有prerequisities，所以总会认为该`clean`文件已经是最新的了，故不会再update）

而Phony会使得make无条件执行该Target。

Phony targets are also useful in conjunction with recursive invocations of `make` (see [Recursive Use of `make`](https://www.gnu.org/software/make/manual/html_node/Recursion.html#Recursion)).



## 命令行参数

|    选项     |          含义          |
| :---------: | :--------------------: |
| -f filename | 指定filename为makefile |
|             |                        |
|             |                        |
|             |                        |
|             |                        |



## 变量和宏

变量，variable，makefile中的变量也常称为宏，macro。

> 变量名大小写敏感。
>
> we recommend using lower case letters for variable names that serve internal purposes in the makefile, and reserving upper case for parameters that control implicit rules or for parameters that the user should override with command options (see [Overriding Variables](https://www.gnu.org/software/make/manual/make.html#Overriding)).3

### 变量类型和定义

其中一种favor可以用变量给变量赋值，变量会递归展开。

```
 variable_a = LoooooongString
 variable_b = ${variable_a}${variable_a}
 variable_c = ${variable_b}${variable_a}
 
 output:
     echo ${variable_c}
     echo ${variable_b}
     echo ${variable_a}
 # make会解析变量里的string，看是否存在形如${}的变量，若存在则展开之，再检查
 # varibale_c = ${a}${a}LoooooongString = LoooooongStringLoooooongStringLoooooongString
```

执行结果：

![image-20210313123834819](file://C:\Users\Five\Desktop\note\img\image-20210313123834819.png?lastModify=1631706564)

这种favor会很灵活，但形如`CFLAGS = $(CFLAGS) -O`的用法会使其陷入无限递归，直至崩溃（Actually `make` detects the infinite loop and reports an error.4）。另一方面，这种favor会降低make的执行效率。



所以有了另一种favor，`Simply expanded variables`，用`:=`或者`::=`定义，两种方法等价。

这种favor下变量在定义时解析，随后拥有一个`string`值，当其再度被调用时，不再解析该string并随着其包含变量而动态更新。

```
 x := a_string
 y := $(x) lalala
 x := updated_string
 
 output:
         echo $x   #单字符变量可以直接用$x的方法调用
         echo $y
```

执行结果：

![image-20210313125534598](file://C:\Users\Five\Desktop\note\img\image-20210313125534598.png?lastModify=1631706564)





### 变量使用

使用变量可以有两种写法`${foo}`和`$(foo)`，当真的需要用到一个dollar符号时，要用两个dollar`$$`符转义，类似C语言的反斜杠。

```
 objects = program.o foo.o utils.o
 program : $(objects)
         cc -o program $(objects)
 
 $(objects) : defs.h
```

> 下面这种奇葩写法也能正确运行（来自官方文档），当然，官方也说：Don’t actually write your makefiles this way!3
>
> ```
>  foo = c
>  prog.o : prog.$(foo)
>       $(foo)$(foo) -$(foo) prog.$(foo)
> ```

还可以定义单字符变量，语法会略微简单，变量使用形如`$x`、`$y`，但一般不推荐。



### 特殊变量

如`MAKEFILE`、`MAKE_RESTARTS`、`MAKE_TERMOUT`、`MAKE_TERMERR`等

又如`DEFAULT_GOAL`、`.RECIPEPREFIX`、`.VARIABLES`、`FEATURES`、`INCLUDE_DIRS`等等。



## 复杂用法

### 条件分支

```
 libs_for_gcc = -lgnu
 normal_libs =
 
 foo: $(objects)
 ifeq ($(CC),gcc)
         $(CC) -o foo $(objects) $(libs_for_gcc)
 else
         $(CC) -o foo $(objects) $(normal_libs)
 endif
```





### 隐含规则







更多内容参考[GNU make官方文档](https://www.gnu.org/software/make/manual/make.html)

# cmake和CMakeLists

如果我们的程序是跨平台的，如果换个平台makefile又要重新修改，这会很麻烦，所以就出现了cmake这个工具，通过cmake我们就可以快速创建出不同平台的makefile文件。

* 自动发现跨平台系统库
* 自动发现和管理工具集
* 支持多种生产工具，如Visual Studio, XCode.

cmake根据CMakeLists.txt来生成makefile文件

```
cmake
make逐条解析
CMakeLists.txt
Makefile
完成编译
```

> makefile是类unix环境下(比如Linux)的类似于批处理的"脚本"文件。其基本语法是: **目标+依赖+命令**，只有在**目标**文件不存在，或**目标**比**依赖**的文件更旧，**命令**才会被执行。由此可见，Makefile和make可适用于任意工作，不限于编程。比如，可以用来管理latex。
>
> Makefile+make可理解为类unix环境下的项目管理工具，但它太基础了，抽象程度不高，而且在windows下不太友好(针对visual studio用户)，于是就有了跨平台项目管理工具cmake
>
> cmake是跨平台项目管理工具，它用更抽象的语法来组织项目。虽然，仍然是目标，依赖之类的东西，但更为抽象和友好，比如你可用math表示数学库，而不需要再具体指定到底是math.dll还是libmath.so，在windows下它会支持生成visual studio的工程，在linux下它会生成Makefile，甚至它还能生成eclipse工程文件。也就是说，从同一个抽象规则出发，它为各个编译器定制工程文件。
>
> cmake是抽象层次更高的项目管理工具，cmake命令执行的CMakeLists.txt文件
>
> qmake是Qt专用的项目管理工具，对应的工程文件是*.pro，在Linux下面它也会生成Makefile。
>
> 作者：玟清 链接：https://www.zhihu.com/question/27455963/answer/36722992 来源：知乎 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# TIGCC

TIGCC is mainly a C compiler for the Texas Instruments TI-89, TI-89 Titanium, TI-92 Plus and Voyage 200 calculators.



# GDB

GNU Debugger.







[^1]:  《Computer System: A Programmer's Perspective》 Randal E. Bryant
[^2]:    http://www.ruanyifeng.com/blog/2015/02/make.html
[^3]:    https://www.gnu.org/software/make/manual/make.html
[^4]:    https://gist.github.com/isaacs/62a2d1825d04437c6f08
[^5]:    gcc和g++是什么关系？ - d41d8c的回答 - 知乎 https://www.zhihu.com/question/20940822/answer/1768772877

