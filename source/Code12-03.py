from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image
import numpy as np

## 함수 선언 부분 ##
def display() :         # Code 12-05.py에서 구현
    pass

def func_open() :       # Code 12-05.py에서 구현
    pass

def func_save() :       # Code 12-06.py에서 구현
    pass

def func_exit() :
    exit()

def func_reverse() :         # Code 12-07.py에서 구현
    pass

def func_bright() :         # Code 12-08.py에서 구현
    pass

def func_dark() :           # Code 12-08.py에서 구현
    pass

def func_gray() :             # Code 12-09.py에서 구현
    pass

def func_bw1():             # Code 12-09.py에서 구현
    pass

def func_bw2() :              # Code 12-09.py에서 구현
    pass

def func_mirror1() :       # Code 12-10.py에서 구현
    pass

def func_mirror2() :       # Code 12-10.py에서 구현
    pass

def func_rotate(times) :   # Code 12-11.py에서 구현
    pass

def func_zoomin() :        # Code 12-12.py에서 구현
    pass

def func_zoomout() :     # Code 12-12.py에서 구현
    pass

## 전역 변수 선언 부분 ##
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []
inW, inH, outW, outH = [0] * 4

## 메인 코드 부분 ##
window = Tk()
window.geometry("500x500")
window.title("넘파이 미니 포토샵")

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "영상 처리(1)", menu = image1Menu)
image1Menu.add_command(label = "반전이미지", command = func_reverse)
image1Menu.add_separator()
image1Menu.add_command(label = "밝게", command = func_bright)
image1Menu.add_command(label = "어둡게", command = func_dark)
image1Menu.add_separator()
image1Menu.add_command(label="회색이미지", command=func_gray)
image1Menu.add_command(label="흑백이미지(127 기준)", command=func_bw1)
image1Menu.add_command(label="흑백이미지(평균값)", command=func_bw2)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="영상 처리(2)", menu = image2Menu)
image2Menu.add_command(label = "상하 반전", command = func_mirror1)
image2Menu.add_command(label = "좌우 반전", command = func_mirror2)
image2Menu.add_separator()
image2Menu.add_command(label = "90도 회전", command = lambda :func_rotate(1))
image2Menu.add_command(label = "180도 회전", command = lambda :func_rotate(2))
image2Menu.add_command(label = "270도 회전", command = lambda :func_rotate(3))
image2Menu.add_separator()
image2Menu.add_command(label = "확대", command = func_zoomin)
image2Menu.add_command(label = "축소", command=func_zoomout)

window.mainloop()