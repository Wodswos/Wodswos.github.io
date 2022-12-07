# 人工智能概述

略

# 机器学习：主要指统计学习

> 赫尔伯特·西蒙曾对“学习”给出以下定义：“如果一个系统能够通过执行某个过程改进他的性能，这就是学习”。按照这一观点，统计学习就是计算机系统通过运用数据及统计方法提高系统性能的机器学习。**现在，当人们提及机器学习时，往往是指统计机器学习。所以可以认为本书介绍的是机器学习方法。**
>
> ——《统计学习方法》李航

机器学习的大致发展主线：

1. 计算机的普及和应用，遇到问题：很难处理非形式化的认识
2. 于是（处理方案）：提出人工智能的概念，并进行早期的实践（）。再遇到问题：效果不好
   1. 具体来说……先略
3. 于是（处理方案）：提出机器学习的概念。再遇到问题：过度依赖人为（专家）进行的特征选取、提取工作（特征工程），即使如此，效果依旧不够好。
   1. 具体来说……先略
4. 于是（处理方案）：提出表示学习的概念，其中尤以深度神经网络表现最佳。



所以 人工智能 —— 机器学习 —— 深度学习 三者不仅是前者包含后者的关系，还带有一丝逐步递进、发展的意味。

## 学习：从数据到知识

知识发现是从数据集中识别出有效的、新颖的、潜在有用的,以及最终可理解的模式的非平凡过程。

知识发现的目的是向使用者屏蔽原始数据的繁琐细节，从原始数据中提炼出有效的、新颖的、潜在有用的知识，直接向使用者报告。

> A computer program is said to learn from experience *E* with respect to some class of tasks *T* and performance measure *P* if its performance at tasks in *T*, as measured by *P*, improves with experience *E*

上述是人称机器学习教父的 Tom Mitchell 给出的对机器学习的定义。即一般来讲，机器学习中的“学习”就是指从经验中学习。





![](C:/Users/Five/Desktop/note/img/v2-2a74db3ed1f2ca0118790a218c423de6_r.jpg)

## 机器学习 vs 数据分析

数据分析这件事可以说自古有之，还有专门的数学门类，即数理统计。

* 人工智能在发展机器学习这一分支的时候，大量地运用了数理统计的方法
* 随着计算机的发展，数理统计/数据分析自然也更多地使用计算机作为统计

结论：

* 数据分析和机器学习（部分）都可以说是计算机和数理统计交叉的产物
* 侧重点各有不同

> 统计学习是概率论、统计学、信息论、计算理论、最优化理论及计算机科学等多个领域的交叉学科，并在发展中住不形成肚子的理论体系与方法论。
>
> —— 《统计学习方法》李航

## 机器学习 vs 数据挖掘[^2]

![](C:/Users/Five/Desktop/note/img/v2-41c66af24c11fbe635667358c1ea456a_hd.jpg)

Data Mining最著名的故事莫过于啤酒和尿布（但应该是编的），

> 开发围棋 AI 那个工程师，可能他围棋水平还不到中级呢，但是搞数据挖掘的，必须精通业务精通场景，工作思路和要求是完全不一样的。
>
> 数据挖掘与机器学习是什么关系？ - 冯国添的回答 - 知乎 https://www.zhihu.com/question/20954873/answer/575322749

也有说从目的区分 Data Mining 和 Machine Learning 的：

* Data Mining: use (huge) data to find property that is interesting
* Machine Learning: use data to compute hypothesis g that approximates target f

> If 'interesting property' same as 'hypothesis that approximate target', then ML=DM (usually what KDDCup Does)
>
> If 'interesting property' related to 'hypothesis that approximate target', them DM can help ML, and vice versa.
>
> Traditional DM also focuses on efficient computation in large database



> A computer program is said to learn from experience *E* with respect to some class of tasks *T* and performance measure *P* if its performance at tasks in *T*, as measured by *P*, improves with experience *E*

上述是人称机器学习教父的 Tom Mitchell 给出的对机器学习的定义。即一般来讲，机器学习中的“学习”就是指从经验中学习。

如何才算从经验中学习呢？是不是可以理解为从经验中得到了新的信息？而这不是跟数据挖掘的定义极其相似吗？两者在定义上就是相近的，两者的研究方法是相通的也就不足为奇了。





在《Introduction to Data Mining》中，主要提到了以下主题

* 什么是数据
  * 相似性和相异性的度量
* 核心的数据挖掘技术
  * 分类
  * 关联分析
  * 聚类分析
* 其他
  * 异常检测
  * 统计检验

在另一本书《Data Mining and Machine Learning: Fundamental Concepts and Algorithms》中也基本类似，分了四Part

* Data Analysis Foundations
* Frequent Pattern Mining
* Clustering
* Classification



似乎暗示着主流的三种方法：分类、聚类、关联分析。

| 比较 | 分类                 | 聚类           | 关联分析       |
| ---- | -------------------- | -------------- | -------------- |
| 数据 | 有标签数据，监督学习 | 无标签，无监督 | 无标签，无监督 |
| 训练 | 需要                 | 不需要         | 不需要         |
| 降维 |                      |                |                |
|      |                      |                |                |



### 数据挖掘之分类

分类显然是最常见的，说烂了的监督学习和函数拟合。

> 总的来说分类是试图发现数据之间的函数、映射关系？

### 数据挖掘之聚类

> 总的来说聚类是试图发现数据之间的类别信息？

### 数据挖掘之关联分析

频繁模式（Frequent Pattern），偏正短语，频繁出现在数据集中的模式（如项集、子序列和子结构等）

关联规则是形如 $X\rightarrow Y$ 的蕴含式



> 总的来说关联分析是试图发现数据之间的结构信息？











# 无监督学习也叫学习？

就算是经典的K-Means这种聚类算法，不也是要先给出K的吗？所以所谓的（非监督）聚类不是相当于一个关于K的最优化函数么？怎么就非监督了？

众所周知，监督学习和无监督学习的分类标准是有无标签。那么问题可以转换，连标签都没有，是不是机器就无法学习？目前而言，在我的理解里答案是偏向于肯定的……没标签，可不就是没法学习吗？



## 压缩感知





## 鸡尾酒会问题

```
[W,s,v] = svd((repmat(sum(x.*x,1),size(x,1),1).*x).*x);
```

# 其他

> 这就是为什么 Hofstadter 说：“一个机器要能理解人说的话，它必须要有腿，能够走路，去观察世界，获得它需要的经验。它必须能够跟人一起生活，体验他们的生活和故事……” 最后你发现，制造这样一个机器，比养个小孩困难太多了，这不是吃饱了没事干是什么。[^1]

## 像半仙算命的演化算法







# 学习资源 & 学习规划

* Categories of Algorithmshttps://static.coggle.it/diagram/WHeBqDIrJRk-kDDY/t/categories-of-algorithms-non-exhaustive
* **每种主要的算法都要重新手写一遍**（当然熟悉 python 里相应的 api 是最基础的）
  * 别人已经完成的，可供参考：
  * https://github.com/Dod-o/Statistical-Learning-Method_Code
  * https://github.com/PRML/PRMLT

## 1.李宏毅 & 吴恩达机器学习课程入门

李宏毅国内搬运 https://www.bilibili.com/video/av59538266

吴恩达国内搬运 https://www.bilibili.com/video/BV19e411W7ga



李宏毅课程的一份笔记（可以当讲义用）：https://datawhalechina.github.io/leeml-notes



## 2.李航统计学习 & 周志华西瓜书巩固加强

可辅以深度之眼相应的训练营课程进行学习。



## 3.Neural Networks and Learning Machine 进阶



还有很经典的：

* 模式识别与机器学习《Pattern Recognition and Machine Learning》
* 《Pattern Classification (2ed)》

但暂时不做考虑



## 4.其他

辅助参考内容：

* 极客时间 王天一  人工智能基础课
* 极客时间 王天一  机器学习40讲
* 极客时间 陈旸  数据分析实战45讲





以及被推荐的：

http://mindhacks.cn/2008/09/11/machine-learning-and-ai-resources/

* 《Programming Collective Intelligence》
* 《AI, Modern Approach 2nd》
* 《The Elements of Statistical Learning》
* 《Foundations of Statistical Natural Language Processing》
* 《Data Mining, Concepts and Techniques》
* 《Managing Gigabytes》
* 《Information Theory: Inference and Learning Algorithms》《信息论、推理与学习算法》Mackay



数学系列：

* 线性代数和矩阵
  * 《矩阵分析》
* 概率
  * 《概率律及其应用》
  * 《All of Statistics》
* 最优化：
  * 《Nonlinear Programming, 2nd》
  * 《Convex Optimization》

还有：

* 《Simple Heuristics that Makes Us Smart》
* 《Bounded Rationality: The Adaptive Toolbox》



还有：

* 吴恩达经典ML课全面升级！更新为Python实现，加入更直观的视觉教学 - 量子位的文章 - 知乎 https://zhuanlan.zhihu.com/p/501258519
* bilibili 机器学习 白板推导系列
* 人工智能 贲可荣、张彦铎编的的那本



## 5.相关文章和问题

为什么在实际的kaggle比赛中，GBDT和Random Forest效果非常好？ - 包包大人的回答 - 知乎 https://www.zhihu.com/question/51818176/answer/2257140440









[^1]:人工智能的局限性 王垠 http://www.yinwang.org/blog-cn/2017/04/23/ai
[^2]:数据挖掘与机器学习是什么关系？ - 知乎 https://www.zhihu.com/question/20954873