import os
import io
str1 = "aaa"
with open("tests.txt","r",encoding='UTF-8') as r:
    cities = r.readlines()
    for city in cities:
        key = city[:-1].split('=')[1]
        value = city[:-1].split('=')[0]
        #print(key)
        #print(value)
        print("'",key,"'",":","'",value,"'",",")
        w = "'"+ key + "'" +":" + "'" + value + "'" + ","+"\n"
        with open('cities1.py','a') as f:
            f.write(str(w))
    r.close()

with open("tests1.docx","w") as w:
    w.write(str1)
