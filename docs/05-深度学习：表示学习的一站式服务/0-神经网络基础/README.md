![](C:/Users/Five/Desktop/note/img/v2-487f13a5de2ef2105a90be878e5f3ed5_720w.jpg)

# 神经网络完成了什么

特征工程一直是机器学习中极为重要的一部分，甚至可以说是关键，而神经网络nb就nb在它可以完成复杂特征的自动提取，即自动化特征工程，而且是自动化复杂的特征工程。

> 相比于传统的特征工程，神经网络不仅自动化，而且还能提取更复杂的特征，几乎可以说百利无一害，自然风头一时无两。


## 特征工程，aka表示学习

Representation Learning。

> Representation learning is a set of methods that allows a machine to be fed with raw data and to automatically discover the representations needed for detection or classification. Deep-learning methods are representation-learning methods with multiple levels of representation, obtained by composing simple but non-linear modules that each transform the representation at one level (starting with the raw input) into a representation at a higher, slightly more abstract level.
> [[来自三巨头的综述：Deep Learning.pdf]]


# 关于神经网络的研究历程

1943年，心理学家McCulloch 和数学家 Pitts 根据神经元提出 M-P 模型，打下坚实基础。

1949年，心理学家 Hebb 提出了人工神经网络的学习规则，称为模型的训练算法的起点。

## 第一代神经网络

1958年，康奈尔大学的心理学家Rosenblatt 发明的感知机（Perceptron）可对输入的多维数据进行二分类，且能够使用梯度下降法从样本（训练集）中进行机器学习（更新权值）。

> 纽约时报（New York Times）的评价：
>
> The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence.

1962年，该方法被证明为能收敛。

1969年，Minsky 和 Papert 发表论文《Perceptron》，从理论上严格证明了单层感知机无法解决异或问题，从而引申到无法解决线性不可分问题，开始陷入对ANN的反思潮。



Arbib 的竞争模型，Kohonen 的自组织映射、Grossberg 的自适应共振模型（ART）、Rumellhart 等人的并行分布处理模型（PDP）等。

## 第二代神经网络

### 循环网络和反馈网络

1982年，Hopfield 提出循环网络，1984年提出 Hopfield 网络，解决了TSP问题。

> Hopfield为反馈式神经网络，区别于现在主流的BP神经网络。

1985年，美国加州大学圣地亚哥分校的 Hinton、Rumellhart 等提出了 Boltzmann机。

### 前馈网络和反向传播算法

1986年，Rumelhart和McCellland为首的科研小组在论文《Learning Representations by back-propagating errors》中首次提出BP算法。

同年，Hiton 提出 MLP 的BP算法，并采用Sigmoid进行非线性映射（激活函数），有效解决了非线性分类和学习的问题，引发了神经网络的第二次热潮。

1989年， Robert Hecht-Nielsen 证明了MLP的万能逼近定理：对于任何闭区间内的一个连续函数F，都可以用含有一个隐含层的BP网络来逼近。

1997年，LSTM模型提出，但并没有引起足够重视。

> 神经网络的第二次热潮逐渐散去，统计学习方法迎来了一段属于他的时代。

## Deep Learning

2006年（**深度学习元年**），Hiton提出了深层网络训练中梯度消失问题的解决方案：无监督训练对权值进行初始化+有监督训练微调。

> 即 Hinton 提出了在非监督数据上建立多层神经网络的一个有效方法，具体分为两步：首先逐层构建单层神经元，这样每次都是训练一个单层网络；当所有层训练完后，使用wake-sleep算法进行调优。
>
> wake阶段：认知过程，通过外界的特征和向上的权重产生每一层的抽象表示，并且使用梯度下降修改层间的下行权重。 
>
> sleep阶段：生成过程，通过顶层表示和向下权重，生成底层的状态，同时修改层间向上的权重。

2011年，ReLU激活函数提出，能够有效抑制梯度消失的问题。

同年，微软首次将深度学习应用在语音识别上。

2012年，Hinton 课题组携 AlexNet 参加 ImageNet图像识别比赛，降维打击夺冠。



扣动了深度学习革命的扳机，神经网络的风头一时无两。





