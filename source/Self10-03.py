import numpy as np
import os
SIZE = 5000  # 원본 크기

## 넘파이 2차원 배열 생성
imageAry = np.random.randint(0, 255, size=(SIZE, SIZE))
np.save('file1', imageAry)
print('### 1. np.save()로 저장한 파일 크기 --> ', os.path.getsize('file1.npy'))

np.savez('file2', imageAry)
print('### 2. np.savez()로 저장한 파일 크기 --> ', os.path.getsize('file2.npz'))

np.savez_compressed('file3', imageAry)
print('### 3. np.savez_compressed()로 저장한 파일 크기 --> ', os.path.getsize('file3.npz'))
