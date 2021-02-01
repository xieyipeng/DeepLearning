import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    # y = x > 0  # 不等号运算
    # return y.astype(np.int)  # 转换数组元素类型
    return np.array(x > 0, dtype=np.int)


if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)

    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # 指定y轴范围
    plt.show()
