

* Mean Squared Error (MSE) 均方差
* Root Mean Squared Error (RMSE) 均方根误差
* Peak Signal-to-Noise Ratio (PSNR) 峰值信噪比
* Structural Similarity Index (SSIM) 结构相似性
* Universal Quality Image Index (UQI) 通用质量图像索引
* Multi-scale Structural Similarity Index (MS-SSIM) 多尺度结构相似性指数
* Erreur Relative Globale Adimensionnelle de Synthèse (ERGAS) 相对全局误差
* Spatial Correlation Coefficient (SCC) 空间相关系数
* Relative Average Spectral Error (RASE) 相对平均光谱误差
* Spectral Angle Mapper (SAM) 光谱角映射
* Visual Information Fidelity (VIF) 视觉信息保真度

# Structural Similarity，SSIM

> 什么是SSIM？ - Young的文章 - 知乎 https://zhuanlan.zhihu.com/p/541385224

SSIM 由 Zhou、Bovik、Sheikh 和 Simoncelli 在 2004 年的一篇论文中介绍，被引用次数约为 38000。用来测试两幅图像的相似性，其测量或者预测图像的质量是基于未压缩的或者无失真的图像作为参考的。

传统检测图像质量的方法 MSE，PSNR（对绝对误差的评估）与人眼的实际视觉感知是不一致的，SSIM算法在设计上考虑了人眼的视觉特性，比传统方式更符合人眼视觉感知。

![](C:/Users/Five/Desktop/note/img/20160714143851293.jpg)
$$
l(x,y) = \frac {2\mu_x \mu_y}{\mu_x^2 + \mu_y^2} \\
c(x,y) = \frac {2\sigma_x \sigma_y}{\sigma_x^2 + \sigma_y^2} \\
s(x,y) = \frac {\sigma _{xy}} {\sigma _x \sigma _y} \\
\mathrm {SSIM}(x,y)  = l(x,y) c(x,y) s(x,y)
$$
其中 $u_x$ 表示图像 A 中的小块 $x$ 的像素强度均值，$\sigma _x^2$ 表示方差；图像 B 中的小块 $y$ 同理；$\sigma _{xy}$ 表示协方差。

实现时添加一些小常数来防止被零除。





