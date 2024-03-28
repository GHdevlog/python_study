import csv
import struct

## 전역 변수부
inRawName = 'c:/CookAnalysis/RAW/cat256.raw'
outRawName = 'c:/CookAnalysis/RAW/cat256_out.raw'
cvsName =  'c:/CookAnalysis/CSV/cat256.csv'
row, col = 256, 256

## 메인 코드부
## RAW --> CSV로 저장
rawFp = open(inRawName, 'rb')
csvFp = open(cvsName,'w', newline='')
csvWriter = csv.writer(csvFp)
csvWriter.writerow(['행', '열', '픽셀 값'])
for i in range(row) :
    for k in range(col) :
        value = int(ord(rawFp.read(1)))
        row_list = [i, k, value]
        csvWriter.writerow(row_list)
rawFp.close()
csvFp.close()

## CSV 파일을 흑백으로
csvFp = open(cvsName,'r')
csvReader = csv.reader(csvFp)
headerList = next(csvReader)
csvList = []
for cList in csvReader :
    value = int(cList[2])
    if value > 128 :
        value = 255
    else :
        value = 0
    csvList.append([cList[0], cList[1], value])

## CSV --> RAW
rawFp = open(outRawName, 'wb')
for cList in csvList :
        x, y, value = map(int , cList)
        rawFp.write(struct.pack('B', value))
rawFp.close()
print('Save. OK~')


