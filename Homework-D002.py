#1. 取出班次一的每一個時間，印出來就好

#2. 將班次一的每一個時間用一個變數保存

#3. 將所有班次和其每一個時間用一個變數保存

#(Hint： 2&3 要想一下用什麼的資料型態做整理比較適合)

import urllib.request

res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/example.csv')

#1. 取出班次一的每一個時間，印出來就好
    # File/IO
    fh = open("./data/example.csv", encoding="utf-8")
    f = fh.read()
    fh.close()
    # print(f)
#CSV READDER
    import csv
    with open("./data/example.csv",encoding="utf-8") as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        for row in rows:
            print(row[5])


#2. 將班次一的每一個時間用一個變數保存


