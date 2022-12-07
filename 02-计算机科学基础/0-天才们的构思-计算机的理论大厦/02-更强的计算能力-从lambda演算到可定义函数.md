> It does not have any complicated formulae or operations. All it ever does is taking a line of letters (or symbols), and performing a little cut and paste operation on it. As you will see, the Lambda Calculus can compute everything that can be computed, just with a very simple cut and paste.
>
> http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html



# 邱奇和计算



## 邱奇论题

也称邱奇-图灵论题，是一个关于可计算性理论的假设。

该假设论述了关于函数特性的，可有效计算的函数值（用更现代的表述来说--在算法上可计算的)。简单来说，邱奇-图灵论题认为“任何在算法上可计算的问题同样可由图灵机计算”。



## Key Point of Lambda Calculus

* functions are values
  * 函数和数一样是一等公民



 Remember that for a calculus, you need to define two things: [^2]

* the syntax, which describes how valid expressions can be written in the calculus
* a set of rules that allow you to symbolically manipulate the expressions.

# Syntax

* 函数定义

```lambda
lambda x . body
```

表示一个参数为x的函数，返回值为body的计算结果，Lambda表达式绑定了参数x。

* 标识符引用

标识符引用就是一个名字，形参。

* 函数应用

```
lambda (x . plus x x) y
```

函数应用写成把函数值放到它的参数前面的形式



## 柯里化-Currying

lambda函数只接受一个参数，如何对多参数进行操作？

**函数本身就是值**。可以写只有一个参数的函数，而这个函数返回一个带一个参数的函数

```lambda
lambda x y . plus x y // 这是比较习惯的写法
lamda x . (lamda y . plus x y)  //单参数写法
```

> 在Python里，会很直观地体会到程序也是数据这一点。函数名本身指代的是一串程序（更本质地说也就是数据），在函数名后加上括号，才表示运行函数，并得到返回值。
>
> 用Python的语法来描述柯里化，就类似如下代码（个人理解）
>
> ```python
> def function_a(x):
>  def function_b(y):
>    	return x + y
>  return function_b
> function(x)(y)  # 最终调用形式
> ```

知道了柯里化可以使得单参数通过嵌套得到多参数，之后完全可以像使用单参数表达式一样使用多参数表达式了，那样语法会更简洁一些。



## Free vs Bound Identifiers

如果一个标识符是一个闭合Lambda表达式的参数，我们则称这个标识符是（被）绑定的。

（可以是当前lambda表达式的参数，也可以是比当前lambda更高级的一个scope，直至可以是全局的）

如果一个标识符在任何封闭上下文中都没有绑定，那么它被称为自由变量。

一个Lambda演算表达式只有在其所有变量都是绑定的时候才完全合法。

# Rules

只有两条：Alpha转换和Beta规约

* Alpha转换：使得递归成为可能。
* Beta规约：使得Lambda演算能够执行任何可以由机器来完成的计算。

## Alpha转换

Alpha转换：变量的名称是不重要的（即形参），可以随时重命名（当然是对这一变量所有的引用同时重命名）

``` lambda
lambda x . if (= x 0) then 1 else x ^ 2
lambda y . if (= y 0) then 1 else y ^ 2  //形参名的变化不影响结果 
```



## Beta规约

这条规则使得Lambda演算能够执行任何可以由机器来完成的计算。

我个人的理解好像就是……可以将实参传给形参然后计算？？

```
(lambda y . (lambda x . x + y)) q
// 规约后：
lambda x . x + q 
```

```
(lambda x y. x y) (lambda z . z * z) 3
// 第一次规约得到（其实就是原路返回）
(lambda z . z * z) 3
// 第二次规约得到
3 * 3
```

Beta规则的形式化写法：

```
lambda x . B e = B[x := e] if free(e) subset free(B[x := e])
```

如果在`B`中绑定的变量和`e`中的自由变量产生命名冲突，我们就需要用Alpha转换来更改标识符名称，使之不同。举例如下：

```
(lambda z . (lambda x . x + z)) (x + 2) 
```

参数x+2中x并没有被定义，是自由变量，但如果盲目地进行beta规约，最终会得到3+3+2，得到了一个结果，这显然不合理。

显然需要系统（就是编程语言的编译器吧）“自动”地发现并利用Alpha转换进行规避这类错误。

最终Beta规约地结果应该是 3+x+2，即里面地形参x被重命名为其他任意something了。

# Lambda演算基本元素[^1]

尽管有了演算表达式，但实际上却连数字都未曾严格引入。

数字并不真正存在于lambda演算中，lambda演算有的只是函数，所以需要某种使用函数创建数字的方式。

## 丘奇数

对于任何数n，它的丘奇数是将其第一个参数应用到第二个参数上n次的函数

即类似于皮亚诺算术的定义，将z视为对零值的命名，而s作为后继函数的名称。

```
0: lambda s z . z
1: lambda s z . s z
2: lambda s z . s ( s z )
```

> **Q:** This is a very strange way of writing numbers...
> **A:** Actually, from the point of view of mathematics, this is not stranger than using the characters 1, 2, 3... and so on, or Roman literals (I, II, III, IV, V...), or Chinese ones (一, 二, 三, 四, 五, ...), or  binary notation (1, 10, 11, 100, 101...). There is no *true* way of writing numbers, there are only conventions. Natural numbers do not care about how we spell them.
>
> http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html

$$
S : \Leftrightarrow \lambda abc.b(abc) \\
\begin{align}
3 S 2 & = (\lambda sz.s(s(s(z)))) (\lambda abc.b(abc)) (\lambda xy.x(x(y))) \\
      & = (\lambda abc.b(abc))((\lambda abc.b(abc))((\lambda abc.b(abc))(\lambda xy.x(x(y))))) \\
      & = (\lambda abc.b(abc))((\lambda abc.b(abc))((\lambda abc.b(abc))(\lambda xy.x(x(y)))))
\end{align} 
$$





## 布尔值和分支

定义布尔值和分支操作

```lambda
let TRUE = lambda x y . x
let FALSE = lambda x y . y
let IfThenElse = lambda cond true_expr false_expr . cond true_expr false_expr 
```

定义逻辑运算

```lambda
let BoolAnd = lambda x y . x y FALSE
let BoolOr = lambda x y . x TRUE y
let BoolNot = lambda x . x FALSE TRUE
```

lambda表达式BoolAnd在三种情况下的运算过程：

`BoolAnd TRUE TRUE` 

1. 展开TRUE：`BoolAnd (lambda x y . x) (lamda x y . x)`
2. alpha变换： `BoolAnd (lambda xa ya . xa) (lambda xb yb . xb)`
3. 展开并beta规约： `(lambda xa ya . xa) (lambda xb yb . xb) FALSE`
4. beta规约： `lambda xb yb . xb`

`BoolAnd TRUE FALSE`

1. 展开False和TRUE：`BoolAnd (lambda x y . x) (lamda x y . y)`
2. alpha变换：`BoolAnd (lambda xa ya . xa) (lambda xb yb . yb)`
3. 展开和beta规约-> (lambda xa ya . xa) (lambda xb yb . yb) FALSE
4. beta规约-> lambda xb yb . yb

`BoolAnd FALSE TRUE`

1. 展开FALSE和TRUE：`BoolAnd (lambda x y . y) (lamda x y . x)`
2. alpha变换： `BoolAnd (lambda xa ya . ya) (lambda xb yb . xb)`
3. beta规约：`(lambda xa ya . ya) (lambda xb yb . xb) FALSE`
4. beta规约： `FALSE`



# 组合子演算

## 递归和Y Combinator



以最简单的阶乘为例，在递归之前还需要定义

* if分支函数IsZero：有三个参数，一个数字，两个值。如果数字为0，则返回第一个值；如果它不为0，则返回第二个值。
* 乘法Multi
* 减一Pred

```
let IsZero n 1 2 . 

lambda n . IsZero n 1 (Mult n ( somthing (Pred n)) )
```

代码种的something显然就是lambda自身，那该如何调用自身呢。

Combinator是一种高阶函数，只引用函数应用。

（一个高阶函数是一个函数，它接受函数作为参数，并且返回的结果也是函数）（隐约记起装饰器模式）

Y Combinator非常特殊，它有近乎神奇的功能使得递归成为可能。

```
let Y = lambda y . (lambda x . y (x x)) (lambda x . y (x x))
```

![](C:/Users/Five/Desktop/note/img/y.jpg)

Y Combinator 的特别之处在于应用自身来创造自身，也就是Y Y = Y (Y Y)

> 也就是说用Y的参数还是Y的话，会死循环呗

`Y Y`工作过程：

1. 展开第一个Y：`(lambda y . (lambda x . y(x x)) (lambda x . y(x x)))Y`
2. beta规约：`(lambda x . Y(x x))(lambda x . Y(x x))`
3. alpha变换：`(lambda xa . Y(xa xa))(lambda xb . Y(xb xb))`
4. beta规约：`Y((lambda xb . Y(xb xb)) (lambda xb . Y(xb xb)))`
5. 展开Y，并作alpha变换，就子子孙孙无穷匮也，`(Y Y) = Y (Y Y) = Y (Y (Y Y))`

对于阶乘，则有

```
let fact = lambda n . IsZero n 1 (Mult n (fact (Pred n)))
let metafact = lambda fact . (lambda n . IsZero n 1 (Mult n (fact (Pred n))))
```



## 关于函数名

在lambda演算中，函数名不是不可缺少的，没有函数名的函数称为匿名函数。lambda符号的引入就是为了去掉函数名这个冗余，使定义匿名函数成为可能。

当需要定义的函数含有递归时，没有函数名意味着用lambda演算无法直接引用函数自身。

一种办法是设计另一个函数G，它接受一个函数作为参数，返回值也是一个函数（这种参数是函数的函数称为高阶函数）。



## K、S、I

- `S`：`S`是一个函数应用组合子： `S = lambda x y z . (x z (y z))`
- `K`：`K`生成一个返回特定常数值的函数： `K = lambda x . (lambda y . x)`。 （即扔掉第二个参数，返回第一个参数）
- `I`：恒等函数： `I = lambda x . x`



# 从Lambda到LISP





# 参考资料

http://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html



[^1]: https://cgnail.github.io/academic/lambda-1/
[^2]: http://goodmath.blogspot.com/2006/06/lamda-calculus-index.html
[^4]:https://goodmath.blogspot.com/
[^8]:How to reinvent the Y combinator https://yinwang0.wordpress.com/2012/04/09/reinvent-y/
[^9]:https://pressron.wordpress.com/2016/08/30/what-we-talk-about-when-we-talk-about-computation/

[^10]:https://existentialtype.wordpress.com/2011/03/16/languages-and-machines/