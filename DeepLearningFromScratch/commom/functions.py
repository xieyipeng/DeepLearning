import numpy as np


def identity_function(x):
    """
    恒等函数
    """
    return x


def step_function(x):
    """
    阶跃函数
    """
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    """
    sigmoid
    """
    return 1 / (1 + np.exp(-x))


def relu(x):
    """
    relu
    """
    return np.maximum(0, x)


def softmax(x):
    """
    softmax
    """
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))


def mean_squared_error(y, t):
    """
    均方误差
    :param y: 输出预测
    :param t: 真实值
    :return: 误差
    """
    return 0.5 * np.sum((y - t) ** 2)


def cross_entropy_error(y, t):
    """
    交叉熵
    :param y: 输出预测
    :param t: 真实值
    :return: 误差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]  # 如果是一维，则除以1
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def cross_entropy_error1(y, t):
    """
    交叉熵，当t非one-hot值
    :param y: 输出预测
    :param t: 真实值
    :return: 误差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]  # 如果是一维，则除以1
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def numerical_diff(f, x):
    """
    数值差分
    :param f: 函数f
    :param x: 点
    :return: 函数f在x点处的导数
    """
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def numerical_gradient1(f, x):
    """
    求偏导数(error)
    :param f:
    :param x: numpy数组
    :return:
    """
    h = 1e-4
    grad = np.zeros_like(x)
    # 多维数组的迭代
    for idx in range(x.shape[0]):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val
    return grad


def numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])  # 多维数组的迭代
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 还原值
        it.iternext()

    return grad


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    """
    梯度下降法
    :param f:
    :param init_x:
    :param lr: 学习率
    :param step_num: 重复次数
    :return:
    """
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x


if __name__ == '__main__':
    a = np.array([1, 2, 3])
    b = np.array([1])
    print(cross_entropy_error1(a, b))
