前端科普系列-Web：一路前行一路忘川 - 无名之辈的文章 - 知乎 https://zhuanlan.zhihu.com/p/91842778

![](C:/Users/Five/Desktop/note/img/v2-50b6a1fde4828f7d3ecaa10004d8c911_b.jpg)

# Web 1.0

略。





# Web 2.0

## Ajax 

Ajax，Asynchronous JavaScript and XML。

JS 脚本可以独立地向服务器请求数据，拿到数据后，进行处理并更新网页，这个过程中，后端只负责提供数据，其他事情都由前端来做，





## 前后端分离

* 前后端分离是一个web架构设计问题
* 架构设计是为了将现实的资源（包括人力资源）进行合理的组合调用并使得最终收益最大化。

> Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.
>
>  - Melvin Conway(1967)





这两年业界说的前后端分离，是限于偏展示类的系统（用A代替），而不是应用、管控类Web项目（用B代替），在B类项目里，前后端是天然分离的，对此，除了少部分后端开发人员，基本所有人的认识都是一致的。[^2]





![](C:/Users/Five/Desktop/note/img/v2-1a16914020e75833279d33c873d74eb1_1440w.jpg)



![](C:/Users/Five/Desktop/note/img/v2-889ced410c2319dbed2fe21c2da6e344_1440w.jpg)









## MVC 和 MVVM

> 参考内容：
>
> https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
>
> https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel
>
> https://developer.mozilla.org/en-US/docs/Glossary/MVC
>
> https://www.techtarget.com/whatis/definition/Model-View-ViewModel

model - view - controller

MVC 模型最核心的一点就是 **所有通信都是单向的**

![](C:/Users/Five/Desktop/note/img/v2-d60d5ecc2ca22a6ebe3b2244b28412cc_b.jpg)





MVVM 同样是一种软件架构模式，它是在 MVC 的基础上演进过来的，去掉了 MVC 中的 Controller，增加了数据的双向绑定。

最有代表性的框架就是 Google 公司推出的 Angular， 它的风格属于 HTML 语言的增强，核心概念就是数据双向绑定。

Vue也可以算是 MVVM 模型



### [MVC on the web](https://developer.mozilla.org/en-US/docs/Glossary/MVC#mvc_on_the_web)

As a web developer, this pattern will probably be quite familiar even if you've never consciously used it before. Your data model is probably contained in some kind of database (be it a traditional server-side database like MySQL, or a client-side solution such as [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).) Your app's controlling code is probably written in HTML/JavaScript, and your user interface is probably written using HTML/CSS/whatever else you like. This sounds very much like MVC, but MVC makes these components follow a more rigid pattern.

Web frameworks such as [AngularJS](https://en.wikipedia.org/wiki/AngularJS) and [Ember.js](https://en.wikipedia.org/wiki/Ember.js) all implement an MVC architecture, albeit in slightly different ways.

## SPA 和 SSR

SPA，Single-Page Application





SSR，Server Side Render

SPA 让 web 变成了应用的形态，它是客户端渲染（client side render）。客户端渲染有它的弊端，譬如没法做 SEO(Search Engine Optimization)，由于所有的 `JS` 和 `CSS`会在首次访问时被全部加载，并且 `HTML` 是在前端组装的，就势必导致首屏加载以及渲染的时间会增加，影响用户体验。

于是，现在又争先恐后的回到服务端渲染



# Web 3.0

略



[^1]: 到底什么是前后端分离？ - 海淀游民的回答 - 知乎 https://www.zhihu.com/question/304180174/answer/557406666
[^2]: Web 前后端分离的意义大吗？ - 徐飞的回答 - 知乎 https://www.zhihu.com/question/28207685/answer/39893889

