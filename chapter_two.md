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

  1. 假设检验：

  > 可根据测试错误率估推出泛化错误率的分布。**恰将ε^个样本误分类**的概率如下式，该式也表达了泛化错误率为ε的学习器被测得**测试错误率为ε^**的概率为：

  ![](https://s1.ax2x.com/2018/04/01/tnGFJ.jpg)

  > 若ε为0.3，则10个样本中测得三个被误分类的概率最大。

  ![](https://s1.ax2x.com/2018/04/01/tnZVn.jpg)

  > 使用**二项检验**来对“ε≤0.3”（即泛化错误率不大于0.3）这样的假设进行检验。