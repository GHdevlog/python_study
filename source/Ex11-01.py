from tkinter import *
from tkinter import ttk
import pandas as pd

## 함수 선언 부
def makeEmptySheet(tabName, r, w, backcolor) :
    retList = []
    for i in range(0, r):
        tmpList = []
        for k in range(0, w):
            if (i==0) :
                ent = Entry(tabName, text='', width=10, background = backcolor )
            else :
                ent = Entry(tabName, text='', width=10,)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수
inFilename = 'C:/CookAnalysis/Excel/singer.xlsx'
df1, df2 = None, None
workSheet1, workSheet2 = [], []
window, baseTab, tab1, tab2 = None, None, None, None

## 엑셀 --> 데이터프레임
xlsx = pd.ExcelFile(inFilename)

sheetName1 = xlsx.sheet_names[0]
sheetName2 = xlsx.sheet_names[1]

df1 = pd.read_excel(inFilename, sheetName1, index_col=None)
df2 = pd.read_excel(inFilename, sheetName2, index_col=None)

window = Tk()
window.geometry('550x150')
window.iconbitmap('excel.ico')

style = ttk.Style(window)
style.configure('TNotebook', tabposition='sw') # nwse
baseTab = ttk.Notebook(window, style='TNotebook')

tab1 = ttk.Frame(baseTab)
baseTab.add(tab1, text=sheetName1)
tab2 = ttk.Frame(baseTab)
baseTab.add(tab2, text=sheetName2)

baseTab.pack(expand=1, fill="both")

workSheet1 = makeEmptySheet(tab1, df1.shape[0]+1, df1.shape[1], 'yellow')
workSheet2 = makeEmptySheet(tab2, df2.shape[0]+1, df2.shape[1], 'aqua')

for i in range(len(df1.columns)) : # 열 이름
    workSheet1[0][i].insert(0, df1.columns[i])
for i in range(len(df2.columns)):  # 열 이름
    workSheet2[0][i].insert(0, df2.columns[i])

for i in range(0, df1.shape[0]) :
    for k in range(0, len(df1.columns)) :
        workSheet1[i+1][k].insert(0, df1.iloc[i][k])
for i in range(0, df2.shape[0]) :
    for k in range(0, len(df2.columns)) :
        workSheet2[i+1][k].insert(0, df2.iloc[i][k])

window.mainloop()