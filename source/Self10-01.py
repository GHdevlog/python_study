import numpy as np
## 파이썬 2차원 리스트 생성
SIZE = 3
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

## 배열을 출력하기
print(numpyAry)
print()

## 배열에 100을 더하기.
numpyAry *= 2

## 배열을 출력하기
print(numpyAry)
print()

sumValue = 0
for i in range(SIZE) :
    for k in range(SIZE) :
        sumValue += numpyAry[i][k]

print('평균 값 --> %7.1f' %  (sumValue / (SIZE * SIZE)))