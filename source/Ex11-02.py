import numpy as np
import matplotlib.pyplot as plt

## 전역 변수
XSIZE, YSIZE = 256, 256
rawFileName = 'C:/CookAnalysis/RAW/cat256.raw'
countArray = np.zeros(256, dtype=np.int32)

## 메인 코드 부분
fp = open(rawFileName, 'rb')
for i in range(0, XSIZE):
    tmpList = []
    for k in range(0, YSIZE):
        data = int(ord(fp.read(1)))
        countArray[data] += 1
fp.close()

x_data = np.arange(256, dtype=np.uint8)
plt.bar( x_data, countArray, color='black')
plt.show()