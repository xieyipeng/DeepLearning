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
