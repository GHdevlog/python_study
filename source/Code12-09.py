from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image
import numpy as np

## 함수 선언 부분 ##
def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    if canvas != None:
        canvas.destroy()

    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, width=outW, height=outH)
    paper = PhotoImage(width=outW, height=outH)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    rgbString = ""
    for i in range(0, outH):
        tmpString = ""
        for k in range(0, outW):
            dataR = outImage[0][i][k]
            dataG = outImage[1][i][k]
            dataB = outImage[2][i][k]
            tmpString += "#%02x%02x%02x " % (dataR, dataG, dataB)  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)
    canvas.pack()

def func_open() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window, filetypes=(("Color 파일", "*.jpg;*.png;*.bmp;*.tif;"), ("모든파일", "*.*")))

    photo = Image.open(filename)  # PIL 객체
    inW = photo.width
    inH = photo.height
    inImage = np.empty((3, inH, inW), dtype=np.uint8)

    photoRGB = photo.convert('RGB')
    for i in range(inH):
        for k in range(inW):
            r, g, b = photoRGB.getpixel((k, i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    outW = inW
    outH = inH
    outImage = inImage.copy()
    display()

def func_save() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg', filetypes=(("JPG 파일", "*.jpg"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    photoRGB = Image.new('RGB', (outW, outH))
    for i in range(outH):
        for k in range(outW):
            r, g, b = outImage[0][i][k], outImage[1][i][k], outImage[2][i][k]
            photoRGB.putpixel( (k,i), (r, g, b, 255))
    photoRGB.save(saveFp.name)

def func_exit() :
    exit()

def func_reverse() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = 255 - inImage
    display()

def func_bright() :
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH = inH
    outW = inW
    value = askinteger("밝게", "값-->", minvalue=-1, maxvalue=255)
    inImage = inImage.astype(np.int16)
    outImage = inImage + value
    outImage = np.where(outImage > 255, 255, outImage)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_dark() :
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH = inH
    outW = inW
    value = askinteger("어둡게", "값-->", minvalue=-1, maxvalue=255)
    inImage = inImage.astype(np.int16)
    outImage = inImage - value
    outImage = np.where(outImage < 0, 0, outImage)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_gray() :
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH = inH
    outW = inW
    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] +  inImage[1] + inImage[2]) / 3  # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3,outH, outW))
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_bw1():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] + inImage[1] + inImage[2]) / 3  # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3, outH, outW))
    outImage = np.where(outImage < 128, 0, 255)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_bw2() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] + inImage[1] + inImage[2]) / 3  # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3, outH, outW))
    value = np.mean(outImage)
    outImage = np.where(outImage < value, 0, 255)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_mirror1() :       # Code 12-12.py에서 구현
    pass

def func_mirror2() :       # Code 12-12.py에서 구현
    pass

def func_rotate(times) :   # Code 12-13.py에서 구현
    pass

def func_zoomin() :        # Code 12-14.py에서 구현
    pass

def func_zoomout() :     # Code 12-14.py에서 구현
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