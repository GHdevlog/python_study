import numpy as np
import matplotlib.pyplot as plt

x_data = ['1st', '2nd', '3rd', '4th', '5th' ]
x_value = np.array([1, 2, 3, 4, 5])
y1_data = np.array([ 90, 28, 75, 58, 78])
y2_data = np.array([ 80, 80, 50, 40, 90])
y3_data = np.array([ 40, 50, 90, 90, 60])

plt.barh( x_value, y1_data, color='red', height=0.1, label='DaHyun')
plt.barh( x_value+0.2, y2_data, color='green', height=0.1, label='JungYoun')
plt.barh( x_value+0.4, y3_data, color='blue', height=0.1, label='MoMo')
plt.yticks(x_value+0.2, x_data)
plt.legend(loc='upper right')
plt.show()