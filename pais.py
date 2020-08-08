import time
import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

conn = sqlite3.connect('db.sqlite3')  # 链接数据库
c = conn.cursor()
c.execute("SELECT * from blog_shujuku")
c.execute("UPDATE blog_shujuku set 买家 = 'Fire'")
conn.commit()