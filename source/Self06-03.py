from tkinter import *

## 함수 선언 부분 ##
def makeEmptySheet(r, w) :
    retList = []
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수 부분 ##
csvList = []
rowNum, colNum = 0, 0
workSheet = []

## 메인 코드 부분 ##
window = Tk()

with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    csvList.append(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        csvList.append(row_list)

rowNum = len(csvList)
colNum = len(csvList[0])
workSheet = makeEmptySheet(rowNum, colNum)

idx = 2 # 인원 수의 인덱스
for i in range(0, rowNum) : # 워크시트에 리스트값 채우기. (= 각 빈 셀에 값 넣기)
    for k in range(0, colNum) :
        if ( csvList[i][idx].isnumeric() ) :
            if ( int(csvList[i][idx]) >= 7) :
                ent = workSheet[i][2]
                ent.configure(bg='magenta')
        workSheet[i][k].insert(0, csvList[i][k])

window.mainloop()
