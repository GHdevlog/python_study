import xlrd
import xlwt

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
outWorkbook = xlwt.Workbook()
idx = 2 # 인원의 인덱스

wsheetList = workbook.sheets()
outSheet = outWorkbook.add_sheet("singer")
worksheet = wsheetList[0]
for col in range(worksheet.ncols):
    outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList :
    for row in range(1, worksheet.nrows) :
        person = worksheet.cell_value(row, idx)
        if int(person) >= 6 :
            totalRow += 1
            for col in range(worksheet.ncols) :
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

outWorkbook.save('c:/CookAnalysis/Excel/outSinger3.xls')
print("Save. OK~")