import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singer165.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                if int(row_list[-2]) >= 165 :
                    csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                if int(row_list[-2]) >= 165:
                    csvWriter.writerow(row_list)

print('Save. OK~')