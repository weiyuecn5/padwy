import time
import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

conn = sqlite3.connect('db.sqlite3')  # 链接数据库
c = conn.cursor()

a=int(input('开始编号:'))
b=int(input('结束编号:'))

def ptj(number):

    full_url = 'http://pad.skyozora.com/pets/' + str(number)

    try:
        r = requests.get(full_url)
        soup = BeautifulSoup(r.text, features="html.parser")
        b = soup.title.text.split('-')
        bb = soup.find('span', class_='yellow bold')
        cwbh=b[0].strip()
        cwmz=b[1].strip()
        cwjz=bb.text
        print(cwbh,cwmz,cwjz)
        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO blog_duizhao (宠物编号,宠物名字,宠物价值,加入时间) VALUES ('%s','%s','%s','%s')" % (cwbh, cwmz, cwjz,t)
        c.execute(sql)
        conn.commit()
    except:
        pass

for i in range(a, b+ 1):
    c.execute("SELECT 宠物名字 FROM blog_duizhao WHERE 宠物编号='%s'" % (str(i)))
    data = c.fetchone()
    print(data)
    if data==None:
        ptj(i)
        print(i)
        sleep(2)
    else:
        print('数据存在:'+str(i))
conn.close()