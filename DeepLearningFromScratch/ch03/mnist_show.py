# TODO: load mnist data
import sys
import os

sys.path.append(os.pardir)
from dataset.minist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)

# TODO: show the first img
import numpy as np
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


img = x_train[0]
label = t_train[0]

print(label)
print(img.shape)
img = img.reshape(28, 28)  # 还原成原来的尺寸
print(img.shape)

img_show(img)
