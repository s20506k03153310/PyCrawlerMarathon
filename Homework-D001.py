#1 （簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
#檔案和API皆是由資料擁有者主動釋出，而爬蟲則是資料擁有者被動公開的。

#2
from urllib.request import urlretrieve
import os
os.makedirs( './Data', exist_ok=True )
urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/Homework.txt")

file = os.listdir('./data/')
if 'Homework.txt' in file:
    print('[O]')
else:
    print('[X]')

with open("./data/Homework.txt","w") as fh:
 f= fh.write("Hello World")
with open("./Data/Homework.txt", "r") as fh:
 f= fh.read()
 print(f)

 if len("Hello world") == len(f):
     print('[o]')
 else:
     print('[x]')