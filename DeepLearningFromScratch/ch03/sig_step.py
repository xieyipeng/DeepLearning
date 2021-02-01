from sigmoid import sigmoid
from step_function import step_function
import numpy as np
import matplotlib.pylab as plt

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = sigmoid(x)
    y2 = step_function(x)

    plt.plot(x, y1)
    plt.plot(x, y2, 'k--')
    plt.ylim(-0.1, 1.1)  # 指定图中绘制的y轴的范围
    plt.show()
