with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    with open("C:/CookAnalysis/CSV/new_singer3.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        tmp_list= header.split(',')
        header_list = []
        for h in tmp_list :
            header_list.append(h.strip())
        idx1 = header_list.index('이름')
        idx2 = header_list.index('국번')
        idx3 = header_list.index('전화 번호')
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if len(row_list[idx3].strip()) != 0 :
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')