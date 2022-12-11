> 推荐阅读：《Groovy in action 2》



Groovy 是 Apache 旗下的一门基于 JVM 平台的动态/敏捷编程语言，在语言的设计上它吸纳了 Python、Ruby 和 Smalltalk 语言的优秀特性，语法非常简练和优美，开发效率也非常高。

> 编程语言的开发效率和性能往往是相互矛盾的，越高级的编程语言封装更多、性能会相应变差，根据需要做出取舍。



Groovy 可以与 Java 语言无缝对接，在写 Groovy 的时候如果忘记了语法可以直接按Java的语法继续写，也可以在 Java 中调用 Groovy 脚本，都可以很好的工作，这有效的降低了 Java 开发者学习 Groovy 的成本。Groovy 也并不会替代 Java，而是相辅相成、互补的关系，具体使用哪门语言这取决于要解决的问题和使用的场景。[^1]



* 构建在强大的Java语言之上 并 添加了从Python，Ruby和Smalltalk等语言中学到的 诸多特征，例如动态类型转换、闭包和元编程（metaprogramming）支持
* 为Java开发者提供了 现代最流行的编程语言特性，而且学习成本很低（几乎为零）。
* 支持DSL（Domain Specific Languages领域特定语言）和其它简洁的语法，让代码变得易于阅读和维护。
* 受检查类型异常(Checked Exception)也可以不用捕获。
* Groovy拥有处理原生类型，面向对象以及一个Ant DSL，使得创建Shell Scripts变得非常简单。
* 在开发Web，GUI，数据库或控制台程序时 通过 减少框架性代码 大大提高了开发者的效率。
* 支持单元测试和模拟（对象），可以 简化测试。
* 无缝集成 所有已经存在的 Java对象和类库。
* 直接编译成Java字节码，这样可以在任何使用Java的地方 使用Groovy。 [2] 
* 支持函数式编程，不需要main函数。
* 一些新的运算符。
* 默认导入常用的包。
* 断言不支持jvm的-ea参数进行开关。
* 支持对对象进行布尔求值。
* 类不支持default作用域，且默认作用域为public。
* groovy中基本类型也是对象，可以直接调用对象的方法。

# 动态调用和MOP





# 闭包





[^1]:https://www.jianshu.com/p/e8dec95c4326