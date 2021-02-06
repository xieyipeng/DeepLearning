import os, sys

sys.path.append(os.pardir)
import numpy as np
from commom.functions import softmax, cross_entropy_error
from commom.functions import numerical_gradient


class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # 两行三列

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss
