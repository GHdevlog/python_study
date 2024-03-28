from tkinter import *
import xlsxwriter

window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture08.gif')
h = photo.height()
w = photo.width()

photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workSheetNames = ['Color', 'GrayScale', 'BlackWhite']
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/picture08_art.xlsx')
workSheetList = []
for workSheetName in workSheetNames :
    workSheetList.append(workbook.add_worksheet(workSheetName))

for worksheet in workSheetList :
    worksheet.set_column(0, w - 1, 1.0)  # 약 0.34
    for i in range(h):
        worksheet.set_row(i, 9.5)  # 약 0.35

worksheet = workSheetList[0]
for i in range(w) :
    for k in range(h) :
        hexR = hex(photoR[i][k])
        hexG = hex(photoG[i][k])
        hexB = hex(photoB[i][k])
        hexStr = '#'
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]

        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

worksheet = workSheetList[1]
for i in range(w) :
    for k in range(h) :
        hexGray = hex(int((photoR[i][k] + photoG[i][k] + photoB[i][k]) / 3))
        hexStr = '#'
        if len(hexGray[2:]) < 2:
            hexStr += ('0' + hexGray[2:]) * 3
        else:
            hexStr += hexGray[2:]*3

        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

worksheet = workSheetList[2]
for i in range(w) :
    for k in range(h) :
        if int((photoR[i][k] + photoG[i][k] + photoB[i][k]) / 3) < 128 :
            hexStr = '#000000'
        else :
            hexStr = '#FFFFFF'

        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

workbook.close()
print('Save. OK~')