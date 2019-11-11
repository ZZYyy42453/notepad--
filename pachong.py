import xlwt as wt
import urllib.request
import re
top250_rank=[]
top250_name=[]
i=0
for i in range(0,10):
    data = urllib.request.urlopen("https://movie.douban.com/top250?start="+str(i*25)+"&filter=").read().decode("utf-8")
    pat='lt="(.*[\u4e00-\u9fa5])'
    #rst=re.compile(pat).findall(data)
    rst2=re.compile(pat).findall(data)
    for j in range(0,25):
        top250_name.append(rst2[j])
print("抓取完毕,等待写入!")

'''
fh=open("C:/Users/zy/Desktop/py_test/movie.txt", "w")
for i in range(0,250):
    fh.write(top250_name[i]+"\n")
fh.close()
'''
workbook=wt.Workbook(encoding='utf-8')
sheet=workbook.add_sheet("豆瓣")
sheet.write(0, 0, "排名")
sheet.write(0, 1, "电影名")
for j in range(1,250):
    sheet.write(j, 0, j)
    sheet.write(j, 1, top250_name[j])
workbook.save("C:\\Users\\zy\\Desktop\\a3.xls")
#work_excel.close()
