* **经验误差与过拟合**

  1. 错误率

  > 分类错误的样本数占样本总数的比例称为“错误率”。更一般的，我们把学习器的实际预测输出和样本的真实输出之间的差异称为“误差”。

  2. 过拟合

  > 当学习器把样本学的太好了，很可能吧样本的自身某个特点当作潜在样本都会具有的一般性质，这样就导致了过拟合。

  ![img](https://img-blog.csdn.net/20180204214320874?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 那么在现实中如何进行模型评估与选择呢？

* **评估方法**

  > 我们只有一个包含m个样例的数据集D={(**x**1,y1),(**x**2,y2)...,(**x**m,ym)}，既要训练，又要测试，怎样才能做到呢？下面介绍几种常见的方法：

  * 留出法

  > 直接将数据集D划分为两个互斥的集合，其中一个作为训练集S，一个作为测试集T。通常采用“分层抽样”使得训练集和测试集的划分的结果分布尽可能一致。常见的一般将2/3~4/5的数据进行训练，剩下的用来测试。

  * 交叉验证法

  > 先将数据集D划分为k个大小相同的互斥子集，每个子集Di都尽可能的保持数据分布的一致性。从而可以进行k次训练和测试，最终返回k次测试结果的均值。该方法通常称为“k折交叉检验法”。

  ![img](https://img-blog.csdn.net/20180204214430401?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 若D中包含m个样本。令k=m，则得到了交叉检验的一个特例：留一法。（留一法的估计结果也未必永远比其他的评估方法准确**（NFL）**）

  * 自助法

  > 自助法是一个比较好的解决方案，她直接以资助采样法为基础。给定包含m个样本的数据集D，对他进行采样获得数据集D‘，之后再将该样本放回D，重复m次，就得到了包含m个数据的数据集D’，显然，一部份样本会在D‘中出现多次。可以做一个简单的估计，样本在m次采样中始终不被采到的概率为：

  ![img](https://img-blog.csdn.net/20180204214523539?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 取极限得：

  ![img](https://img-blog.csdn.net/20180204214542338?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 也就是说，初始数据集D中约有36.8%的样本未出现在采样数据集D’中。

  > 将D’用作训练集，D\D’**（“\”代表集合减法）**用作测试集；这样，实际评估的模型与期望评估的模型都使用m个训练样本，而我们仍有数据总量约1/3的、没在训练集中出现的样本用于测试。这样的测试结果，称为“包外估计”。

  > 自助法在数据集较小、难以有效划分训练/测试集时很有用；而在初始数据量足够时，留出法和交叉验证法更常用一些。

  * 调参与最终模型

  > 在进行模型评估与选择时，除了要对使用学习算法进行选择，还需对算法参数进行设定，这就是通常所说的“参数调节”或简称“调参”。
  >
  > 在现实中常用的做法，是对每个参数选定一个范围和变化步长。显然，有的时候选定的参数值往往不是“最佳”值，但这是在计算开销和性能估计之间进行折中的结果，通过这个折中，学习过程才变得可行。事实上，即便在进行这样的折中后，调参往往仍很困难。
  >
  > 另外，需注意的是，我们通常把学得模型在实际使用中遇到的数据称为测试数据，为了加以区分，模型评估与选择中用于评估测试的数据集常称为“验证集”。

* **性能度量**

  > 在预测任务中，给定样例的数据集D={(**x**1,y1),(**x**2,y2)...,(**x**m,ym)}，其中yi表示是示例**x**i的真是标记，要评估学习器的性能，就要把学习器的预测结果f(**x**)与真实标记y进行比较。

  > 回归任务中最常用的度量是“均方误差”：

  ![img](https://img-blog.csdn.net/20180207011215596?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 对于数据分布D和概率密度函数p(·)，均方误差可描述为

  ![img](https://img-blog.csdn.net/20180207011234951?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 下面主要介绍分类任务中常用的性能度量:

  * 错误率与精度

  > 若样本总数为m，则错误率为：

  ![img](https://img-blog.csdn.net/20180207011308955?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 精度为：

  ![img](https://img-blog.csdn.net/20180207011407020?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 对于数据分布D和概率密度函数p(·)，错误率与精度为:

  ![img](https://img-blog.csdn.net/20180207011505461?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  * 查准率和查全率

  > 查准率：检索出的信息有多少比例是用户感兴趣的。查准率是在讲，挑出的好瓜里头，有多少真的是好瓜。
  >
  > 查全率：用户感兴趣的信息中有多少被检索出来了。查全率是在讲，挑出来真的好瓜，占总共好瓜个数的多少。

  > 查准率和查全率更适合此类需求的性能度量。
  >
  > 对于二分类问题，可将样例根据真是类别和学习器预测类别组合划分：

  ![img](https://img-blog.csdn.net/20180207011603399?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 查准率P(precision)：

  ![img](https://img-blog.csdn.net/20180207011631552?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 查全率R(recall)：

  <img alt="" src="https://img-blog.csdn.net/20180207011650173?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast">

  > 一般来说，查准率高时，查全率往往偏低；而查全率高时，查准率往往偏低。通常只有在一些简单任务中，才可能使查准率和查全率都很高。

  > 根据学习器的预测结果对样例进行排序，排在前面的是学习器认为“最可能”是正例的样本，排在后面的则是学习器认为“最不可能”是正例的样本。按此顺序逐个**把样本作为正例**进行预测，则每次可以计算出当前的查全率、查准率。以查准率为纵轴、查全率为横轴作图，就得到了查准率-查全率曲线，简称“P-R曲线”，显示该曲线的图称为“P-R图”：

  ![img](https://img-blog.csdn.net/20180207011718649?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 若一个学习器的P-R曲线被另一个学习器的曲线完全“包住”，则可断言后者的性能优于前者；如果两个学习器的P-R曲线发生了交叉，则难以一般性地断言两者孰优孰劣，只能在具体的查准率或查全率条件下进行比较。然而，在很多情形下，人们往往希望把学习器A与B比出个高低。这时一个比较合理的判据是**比较P-R曲线下面积的大小**，它在一定程度上表征了学习器在查准率和查全率上取得相对“双高”的比例。

  > 但是这个值不太容易估算，因此人们就设计出了“平衡点”（**Break-Even Point**，简称BEP），它是综合考查准率、查全率的性能度量，它是“查准率=查全率”时的取值。

  > 但是BEP还是过于简化了些，更常用的是F1度量：（基于P和R的调和平均得来）

  ![img](https://img-blog.csdn.net/20180207011810783?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 在一些应用中，对查准率和查全率的重视程度有所不同。F1度量的一般形式![img](https://img-blog.csdn.net/20180207011831332?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)，能让我们表达出对查准率/查全率的不同偏好，它定义为:

  ![img](https://img-blog.csdn.net/20180207011856226?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 其中β>0度量了查全率对查准率的相对重要性。
  >
  > ①β=1  退化为标准的F1
  >
  > ②β>1  查全率有更大影响
  >
  > ③β<1  查准率有更大影响

  > 很多时候我们有多个二分类混淆矩阵，当我们希望在n个二分类混淆矩阵上综合考察查准率和查全率的时候，一种直接的做法是先在各混淆矩阵上分别计算出查准率和查全率，记为![img](https://img-blog.csdn.net/20180207011925801?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)，再计算平均值，这样就得到“宏查准率”、“宏查全率”，以及相对应的“宏F1”：

  ![img](https://img-blog.csdn.net/20180207011949606?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 也可以先将各混淆矩阵的对应元素进行平均，得到TP、FP、TN、FN的平均值，分别记为![img](https://img-blog.csdn.net/20180207012044069?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)，再基于这些平均值计算出“微查准率”、“微查全率”、“微F1”：

  ![img](https://img-blog.csdn.net/20180207012021758?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  * ROC与AUC

  > 很多学习器是为测试样本产生一个实值或概率预测，然后将这个预测值与一个分类阈值进行比较，若大于阈值则分为正类，否则为反类。实际上，根据这个实值或预测结果，我们可将测试样本进行排序，“最可能”是正例的排在最前面，“最不可能”是正例的排在最后面，这样，分类过程就相当于在这个排序中以某个“截断点”将样本分为两部分，前一部分判作正例，后一部分则判为反例。

  > ROC全称是“**受试者工作特征**”，其ROC曲线则是从这个角度出发来研究学习器泛化性能的有力工具。

  > 与上一点介绍的P-R曲线相似，我们根据学习器的预测结果对样例进行排序，按此顺序逐个把样本作为正例进行预测，每次计算出两个重要量的值，分别以它们为横、纵坐标作图，就得到了“ROC曲线”。与P-R曲线使用查准率、查全率为纵、横轴不同，ROC曲线的纵轴是“真正例率”（简称TPR），横轴是“假正例率”（FPR），两者分别定义为：

  ![img](https://img-blog.csdn.net/20180207012118497?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  ![img](https://img-blog.csdn.net/20180207012153981?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 进行学习器的比较时，与P-R图相似，若一个学习器的ROC曲线被另一个学习器的曲线完全“包住”，则可断言后者的性能优于前者；若两个学习器的ROC曲线发生交叉，则难以一般性地断言两者孰优孰劣。此时如果一定要进行比较，则较为合理的判据就是比较ROC曲线下的面积，即**AUC**（Area Under ROC Curve）:

  ![img](https://img-blog.csdn.net/20180207012310640?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > AUC考虑的是样本预测的排序质量，因此它与排序误差有紧密联系。给定个![img](https://img-blog.csdn.net/20180207012340440?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)正例和![img](https://img-blog.csdn.net/20180207012414759?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)个反例，令![img](https://img-blog.csdn.net/20180207012435205?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)和![img](https://img-blog.csdn.net/20180207012453861?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)分别表示正、反例集合，则排序“损失”定义为：

  ![img](https://img-blog.csdn.net/20180207012513202?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  ​

  > 即考虑每一对正、反例，若正例的预测值小于反例，则记一个“罚分”，若相等，则记0.5个罚分。容易看出，![img](https://img-blog.csdn.net/20180207012739091?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)对应的是ROC曲线之上的面积：若一个正例在ROC曲线上对应标记点的坐标为（x,y），则x恰是排序在其之前的反例所占的比例，即假正例率。因此有：

  ![img](https://img-blog.csdn.net/20180207012753950?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  * **代价敏感错误率与代价曲线**

  > 在现实任务中，不同类型的错误所造成的后果不同。为**权衡不同类型错误所造成的不同损失**，可为错误赋予“非均等代价”。

  > 以二分类任务为例，我们可根据任务的领域知识设定一个“代价矩阵”，如表2.2所示，其中![img](https://img-blog.csdn.net/20180207012840106?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)表示将第i类样本预测为第j类样本的代价。一般来说![img](https://img-blog.csdn.net/20180207012901401?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)=0；若将第0类别为第1类所造成的损失更大，则![img](https://img-blog.csdn.net/20180207012919069?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)>![img](https://img-blog.csdn.net/20180207012943094?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)；损失程度相差越大，![img](https://img-blog.csdn.net/20180207012919069?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)与![img](https://img-blog.csdn.net/20180207012943094?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)值的差别越大。不过在一般情况下，重要的是代价比值而非绝对值，例如![img](https://img-blog.csdn.net/20180207012919069?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)：![img](https://img-blog.csdn.net/20180207012943094?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)=5:1与50:10所起效果相当。

  ![img](https://img-blog.csdn.net/20180207013145345?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 在非均等代价下，我们所希望的不再是简单地最小化错误次数，而是希望**最小化“总体代价”**，若将表2.2中的第0类作为正类，第1类作为反类，令![img](https://img-blog.csdn.net/20180207013247337?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)与![img](https://img-blog.csdn.net/20180207013302169?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)分别代表样例集D的正例子集和反例子集，则“代价敏感”错误率为：

  ![img](https://img-blog.csdn.net/20180207013340835?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 在非均等代价下，**ROC曲线不能直接反映出学习器的期望总体代价**，而“代价曲线”则可达到该目的。代价曲线图的横轴是取值为[0,1]的正例概率代价

  ![img](https://img-blog.csdn.net/20180207013416479?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  > 正例的概率代价除以总的概率代价。

  > 其中p是样例为正例的概率；纵轴是取值为[0,1]的归一化代价

  ![img](https://img-blog.csdn.net/20180207013447841?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVpemFvU1lVQUNN/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  >  FPR是假正例率，FNR假反例率。

  ![2017-09-02_165517.png-62.9kB](http://static.zybuluo.com/zzw1992/kbida8wb3axkkbpoznnro90j/2017-09-02_165517.png)

  * 解释：

  > 对于**正例概率代价**:
  >
  > 将正例概率代价上下同时乘以N，其中分母N×p×cost01+N×(1−p)×cost10N×p×cost01+N×(1−p)×cost10表示样本集中**所有正例都被认为是反例的代价与所有反例都被划分成正例的代价之和**，也就是样本划分的最大代价。分子表示**所有正例都被认为是反例的代价**。
  >
  > 这个比率，就是**正例划分错误的代价在最大总体代价下的比例**。当P(+)cost=0P(+)cost=0时，即p=0p=0,说明样本中没有正例。当P(+)cost=1P(+)cost=1时，即p=1p=1,说明样本中没有反例。 
  >
  > 对于**归一化代价**：
  >
  > 将之也上下同时乘以样本数量NN，则N×FNR×p×cost01=N×p×FNR×cost01，N×p是**正样例的数目**，FNR是正样例中被误判为反例的数目。所以分子的第一部分是在某一阈值p下，将正例判别为反例的代价。同理第二部分可以看成是在阈值p下，将反例判为正例的代价。因此，**分子部分**的和表示算法**f**在某一阈值p下的**总代价**。 当p=0时，P(+)cost=0，costnorm=FPR；同理，当p=1时，P(+)cost=1，costnorm=FNR； 
  >
  > **看到这里，感觉样本集DD中，正例比例pp对预测算法ff的好坏并没有太大影响。**
  >
  > FPR与FNR的连线上的任一点，其横坐标对应某一正概率代价P(+)cost∗P(+)cost∗，纵坐标就是在该正概率代价、FPR、FNR下的预期损失。 
  >
  > 图中的阴影部分，也就是期望总体代价那一部分，可以说是**在任一正例概率p下，无论FPR和FNR如何变化，算法都必须付出的代价**。

* **比较检验**

  涉及多个方面

  - 希望比较为泛化性能，而实验评估的是测试集上的性能，两者未必相同
  - 测试集上的性能与测试集的选择有很多关系
  - 很多机器算法有一定的随机性，即使相同参数训练也可以会结果不同

  > 统计假设检验为我们进行学习器的性能比较提供了重要依据。本节默认用错误率为性能度量，用ε表示。

  1. **假设检验：**

  > 可根据测试错误率估推出泛化错误率的分布。**恰将ε^个样本误分类**的概率如下式，该式也表达了泛化错误率为ε的学习器被测得**测试错误率为ε^**的概率为：

  ![](https://s1.ax2x.com/2018/04/01/tnGFJ.jpg)

  ![](https://s1.ax2x.com/2018/04/02/6zRtH.jpg)

  > 若ε为0.3，则10个样本中测得三个被误分类的概率最大。

  ![](https://s1.ax2x.com/2018/04/01/tnZVn.jpg)

  * **引入偏导数**

  > * **偏导数**
  >
  > 在数学中，一个多变量的函数的偏导数，就是它关于其中一个变量的导数而保持其他变量恒定（相对于全导数，在其中所有变量都允许变化）。
  >
  > 在 xOy 平面内，当动点由 P(x0,y0) 沿不同方向变化时，函数 f(x,y) 的变化快慢一般说来是不同的，因此就需要研究 f(x,y) 在 (x0,y0) 点处沿不同方向的变化率。
  >
  > 在这里我们只学习函数 f(x,y) 沿着**平行于 x 轴**和**平行于 y 轴**两个特殊方位变动时， f(x,y) 的变化率。
  >
  > 偏导数的表示符号为:∂。
  >
  > 偏导数反映的是函数沿[坐标轴](https://baike.baidu.com/item/%E5%9D%90%E6%A0%87%E8%BD%B4)正方向的变化率。
  >
  > * **偏导数的求法**
  >
  > 当函数 z=f(x,y) 在 (x0,y0)的两个偏导数 f'x(x0,y0) 与 f'y(x0,y0)都存在时，我们称 f(x,y) 在 (x0,y0)处可导。如果函数 f(x,y) 在域 D 的每一点均可导，那么称函数 f(x,y) 在域 D 可导。
  >
  > 此时，对应于域 D 的每一点 (x,y) ，必有一个对 x (对 y )的偏导数，因而在域 D 确定了一个新的二元函数，称为 f(x,y) 对 x (对 y )的偏导函数。简称偏导数。
  >
  > 按偏导数的定义，将多元函数关于一个自变量求偏导数时，就将其余的自变量看成常数，此时他的求导方法与一元函数导数的求法是一样的。
  >
  > 在多元函数的求导中，求的是偏导数，方法依然是这三个法则，尤其是链式求导法则，是我们自始至终必须使用的法则。无论是隐函数，还是显函数，或是复合函数，均是如此。 显函数 = explicit function；隐函数 = implicit function；复合函数 = composite function。
  >
  > **例一**
  >
  > ![](https://s1.ax2x.com/2018/04/02/6VO63.png)
  >
  > **例二**
  >
  > ![](https://s1.ax2x.com/2018/04/02/6VsMG.png)
  >
  > **例三* *
  >
  > ![](https://s1.ax2x.com/2018/04/02/6VuLn.png)

  > 对**P**求偏导数，得：

  ![](https://s1.ax2x.com/2018/04/02/6VQYl.jpg)

  > 可以使用**二项检验**来对“ε≤0.3”（即泛化错误率不大于0.3）这样的假设进行检验。即：对错误率小于定值定值a这样的假设进行检验。
  >
  > 具体计算时只需把错误样本数大于3的概率求和，看是否小于α即可。更一般的：

  ![](https://s1.ax2x.com/2018/04/02/6V4RE.jpg)

  * **t检验：**

  > 很多时候并不做一次留出法估计，而是多次重复留出法或是交叉检验法等进行多次训练/测试，得到多个测试错误率，此时可使用“**t检验**”
  >
  >  错误率都集中分布在某个定值周围的检验手段（度娘具体介绍：[t分布](http://baike.baidu.com/link?url=pT2OT1DAkeSzXfadPTMY1XXpPalQuypXqRcA8w1PGKO4cRTbPOWYZJqAdpjTKUSZDcEG05aEC3Pbkr0YwjBW74wjxBsEf_OBF2ZwfbnStd3)）

  * **引入t分布**

  > 在[概率论](https://baike.baidu.com/item/%E6%A6%82%E7%8E%87%E8%AE%BA/829122)和[统计学](https://baike.baidu.com/item/%E7%BB%9F%E8%AE%A1%E5%AD%A6/1175)中，学生**t-分布**（*t*-distribution），可简称为*t*分布，用于根据小样本来估计呈[正态分布](https://baike.baidu.com/item/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83)且方差未知的总体的均值。如果总体方差已知（例如在样本数量足够多时），则应该用正态分布来估计总体均值。
  >
  > t分布曲线形态与n（确切地说与自由度df）大小有关。与标准正态分布曲线相比，自由度df越小，t分布曲线愈平坦，曲线中间愈低，曲线双侧尾部翘得愈高；自由度df愈大，t分布曲线愈接近正态分布曲线，当自由度df=∞时，t分布曲线为标准正态分布曲线。

  ![](https://s1.ax2x.com/2018/04/02/6YBQE.jpg)

  > 以上两种方法都是对关于单个学习器泛化性能的假设进行检验，现实中更多的需要对不同学习器的性能进行比较下面介绍适用于此类情况的检验方法。

  2. **交叉验证t检验**

  > 即“**成对t检验**”。
  >
  > 基本思想是**如果两个学习器性能相同，则他们使用相同的训练/测试集得到的错误率应该相同**。
  >
  > 具体方法：对“学习器A和B性能相同”这个假设做t检验，计算出均值和方差，如果小于某个你定的阈值，那么就可以认为是相同，否则**取平均错误小的那个作为性能更优**的模型。

  ![](https://s1.ax2x.com/2018/04/02/6YbXq.jpg)

  > 想要进行有效的检验，一个重要的前提是测试错误率均为繁华错误率的独立采样。但是通常情况下由于样本有限，交叉验证时训练集有部分的重叠，就使得测试错误率实际上不独立，为缓解这个问题，我们可采用**5×2交叉验证**。

  * 5×2交叉验证是做5次2折交叉检验。

  > 为缓解测试错误率的不独立性

  ![](https://s1.ax2x.com/2018/04/03/6pbE6.jpg)

  > 服从自由度为5的t分布，其双边检验临界值tα/2，5当α=0.05时，为2.5706，α=0.1时，为2.0150。

  * McNemar检验

  ![](https://s1.ax2x.com/2018/04/04/6CdiX.png)

  > McNemar检验考虑变量：

  ![img](https://s1.ax2x.com/2018/04/03/6p2Hi.png)

  > 服从自由度为1的卡方分布，即标准正态分布的平方。自由度为1的卡房检验的临界值当α=0.05时为3.8415，α=0.1时为2.7055。

  * Friendman检验和Nemenyi检验

  > 假定D1、D2、D3、D4是个数据集对算法A、B、C进行比较，使用留出法或交叉验证法得到算法在每个数据集上的测试结果，在每个数据集上根据性能排序，并赋值1，2，3等，若测试性能相同，则平分序值，得到如下表格：

  ![](https://s1.ax2x.com/2018/04/04/6Chcn.png)

  > 使用Friendman检验判断算法性能是否相同。若是相同的话，他们的平均序值也应该是相同的。假定在N个数据集上比较k个算法，ri表示第i个算法的平均序值。那么平均序值ri的均值和方差分别为(k+1)/2和(k*k-1)/12。变量：

  ![](https://s1.ax2x.com/2018/04/04/6CEbS.png)

  > 在K和N都较大时，服从自由度为k-1的卡方分布。但是原始的Friendman检验过于保守，常使用变量：

  ![](https://s1.ax2x.com/2018/04/04/6CAx9.png)

  > 其中φx*x，由上上式得到

  ​

  ​

  ​

  ​