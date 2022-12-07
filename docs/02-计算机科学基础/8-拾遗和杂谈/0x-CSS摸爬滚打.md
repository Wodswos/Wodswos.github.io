主要是个人博客需要，现成的模板又不好用，勉为其难继续碰一碰前端的东西。

# 选择器

主要选择器有如下：

* `.class`：类选择器
* `#id`：唯一ID选择器
* `*`：选择所有元素
* `element`：标签选择器，选择所有element的标签
* `element1,element2`：element1和element2
* `element1 element2`：element1内的所有element2
* `element1>element2`：所有父级元素是element1的element2
* `element1+element2`：紧接着element1的element2
* `[attribute]`
* `[attribute=value]`
* `[attribute~=value]`



## 优先级

css可以继承自祖先，也可以直接指定，也可以通过选择器赋予，不同方式之间优先级有先后。





# 布局

## 定位

`position`属性的值默认为`static`，即没有定位，元素出现在正常的文档流中。设置`left\right\bottom\top`等偏移属性是无效的。`z-index`属性也不会生效。

设置了绝对定位的元素，在文档流中是不占据空间的，如果某元素设置了绝对定位，那么它在文档流中的位置会被删除，那这个元素到哪去了呢？它浮了起来，其实设置了相对定位relative时也会让该 元素浮起来，但它们的不同点在于，相对对定位不会删除它本身在文档流中占据的那块空间，而绝对定位则会删除掉该元素在文档流中的位置，完全从文档流中抽了出来，我们可以通过z-index来设置它们的堆叠顺序 。

它的定位就是相对于设置了除static定位之外的定位（比如position:relative）的第一个祖先元素，如果所有的祖先元素都没有以上三种定位中的其中一种定位，那么它就会相对于文档body来定位。

相对于窗口定位的是fixed。



* 绝对定位
* 相对定位







## 导航栏

### ::after和::before

为了自己写个导航栏，于是去研究别人的导航栏，看到很多`::before`和`::after`这样的代码。

* 伪元素

# 盒子模型

一般每个块级元素都有三个盒子层层包裹。

## margin

最外层Margin



## padding





## border