import numpy as np
import matplotlib.pyplot as plt

SIZE = 30
x_value = np.random.rand(SIZE)
y_value= np.random.rand(SIZE)
sizeAry = (50 * np.random.rand(SIZE))**2
colorAry = np.random.rand(SIZE)

plt.scatter(x_value, y_value, s=sizeAry, c=colorAry, alpha = 0.5, cmap='spring')
plt.colorbar()
plt.show()