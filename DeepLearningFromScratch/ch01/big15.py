import numpy as np

X = np.array([[12, 23], [34, 45]])
X = X.flatten()  # 扁平
print(X[X > 15])
