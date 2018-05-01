# 良/恶性乳腺癌肿瘤预测
import pandas as pd

# 调用pandas工具包的read_csv函数/模块，传入训练文件地址参数，获得返回的数据并存放至de_train
df_train = pd.read_csv(r'F:\github\MachineLearning\pythonMachineLearningAndTrain\src\breast-cancer-train.csv')
df_test = pd.read_csv(r'F:\github\MachineLearning\pythonMachineLearningAndTrain\src\breast-cancer-test.csv')

# 选取‘Clump Thickness’和‘Cell Size’作为特征，构建测试集中的正负分类样本
df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]

# 导入matplotlib工具包的pyplot并化简为plt
import matplotlib.pyplot as plt

# 绘制良性肿瘤的样本点，标记为红色。
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='०', s=200, c='red')
# 恶性标记为黑色
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')

# 绘制x，y轴的说明
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
# 显示图
plt.show()

# 导入numpy工具包，命名为np
import numpy as np

# 利用numpy中的random函数，随机采样直线的截距和系数
intercept = np.random([1])
coef = np.random.random([2])
lx = np.arange(0, 12)
ly = (-intercept - lx * coef[0]) / coef[1]
# 绘制一条随机直线
plt.plot(lx, ly, c='yellow')

# 绘制图
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='०', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
# 显示图
plt.show()

# 导入sklearn中的逻辑斯蒂回归分类器
