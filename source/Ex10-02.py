import numpy as np
from tkinter import *

## 함수 선언부
def displayImage(imageR, imageG, imageB) :
    rgbString = ""
    for i in range(0, h) :
        tmpString = ""
        for k in range(0, w) :
            dataR = imageR[k][i]
            dataG = imageG[k][i]
            dataB = imageB[k][i]
            tmpString += "#%02x%02x%02x " % (dataR, dataG, dataB) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

## 전역 변수부
window = None
canvas = None
w, h = 0, 0
photoR, photoG, photoB = None, None, None # 2차원 넘파이 배열

## 메인 코드부
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture24.gif')
h = photo.height()
w = photo.width()

window.title("GIF 사진 처리")
canvas = Canvas(window, height = h, width = w)
paper = PhotoImage(height = h, width = w)
canvas.create_image((w/2, h/2), image = paper, state = "normal")

photoR=np.empty((w, h), dtype=np.uint8)
photoG=np.empty((w, h), dtype=np.uint8)
photoB=np.empty((w, h), dtype=np.uint8)

## (1)원본 추출 및 출력
for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b
displayImage(photoR, photoG, photoB)

## (2) 반전 처리 및 출력
photoR = 255 - photoR
photoG = 255 - photoG
photoB = 255 - photoB
displayImage(photoR, photoG, photoB)

## (3) 회색영상 처리 및 출력
photoRGB =  (photoR.astype(np.uint16) + photoG.astype(np.uint16)  + photoB.astype(np.uint16) )
photoRGB =  photoRGB / 3
photoRGB = photoRGB.astype(np.uint8)
photoR = photoG = photoB = photoRGB
displayImage(photoR, photoG, photoB)

## (4) 흑백 처리 및 출력
photoR = np.where(photoR < 128, 0, 255)
photoG = np.where(photoR < 128, 0, 255)
photoB = np.where(photoR < 128, 0, 255)
displayImage(photoR, photoG, photoB)

canvas.pack()
window.mainloop()