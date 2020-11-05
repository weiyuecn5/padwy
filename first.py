import sqlite3
import os,shutil,time


# 这是处理数据库的脚本

# 1.批量修改 是否已卖状态 默认值为0,已卖为1
def isbuy():
    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()
    c.execute("UPDATE pad_shujuku set 已卖 = '0' where 已卖='1'")
    print('完成')
    conn.commit()
    conn.close()

# 2.批量升级数据 未上传为0,上传了为1
def upshuju():
    if os.path.isfile('db1.sqlite3'):
         os.remove('db1.sqlite3')
         shutil.copyfile('db.sqlite3','db1.sqlite3')
    else:
        shutil.copyfile('db.sqlite3', 'db1.sqlite3')

    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()

    conn1 = sqlite3.connect('db1.sqlite3') #链接数据库
    d = conn1.cursor()

    datas=d.execute("SELECT * from pad_huancun")
    for data in datas:
        if data[5]=='1':
            print(data[0],data[1],data[2],data[3],data[4],data[6])
            c.execute("SELECT 宠物 FROM pad_shujuku WHERE 账号编号='%s'"%(data[1]))
            ycw=c.fetchone()
            # print(ycw)
            # if 699<int(data[2])<800:
            #     stsl=data[2].replace('7','2',1)
            # else:
            #     stsl=data[2]    #石头数量处理,把7 改成 2
            if ycw==None:
                xcw = data[4] + ','
                sql="INSERT INTO pad_shujuku (账号编号,石头数量,等级,宠物,更新时间,买家,价格,已卖) VALUES ('%s','%s','%s','%s','%s',' ',' ','0')"%(data[1],stsl,data[3],xcw,data[6])
                c.execute(sql)
                c.execute("UPDATE pad_huancun set 是否上传 = '0' where 唯一键='%s'" % (data[0]))
            else:
                xcw = ycw[0] + data[4] + ','
                sql = "UPDATE pad_shujuku set 石头数量 = '%s',等级='%s',宠物='%s',更新时间='%s' where 账号编号='%s'"%(stsl,data[3],xcw,data[6],data[1])
                c.execute(sql)
                c.execute("UPDATE pad_huancun set 是否上传 = '0' where 唯一键='%s'"%(data[0]))
            conn.commit()
        # break
        # time.sleep(0.05)
    conn.close()

#迁移数据
def copyshuju():
    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()
    conn1 = sqlite3.connect('db2.sqlite3') #链接数据库
    d = conn1.cursor()
    datas=d.execute("SELECT * from pad_shujuku")
    for data in datas:
        print(data[0], data[1], data[2], data[3], data[4])
        sql = "INSERT INTO blog_shujuku (账号编号,石头数量,等级,更新时间,宠物,已卖,买家,价格) VALUES ('%s','%s','%s','%s','%s','%s','','')" % (
            data[0], data[1], data[2], data[3], data[4],'否')
        c.execute(sql)
        conn.commit()
        # break
    conn.close()

def copyduizhao():
    conn = sqlite3.connect('db.sqlite3') #链接数据库
    c = conn.cursor()
    conn1 = sqlite3.connect('db1.sqlite3') #链接数据库
    d = conn1.cursor()
    datas=d.execute("SELECT * from blog_duizhao")
    for data in datas:
        print(data[0],data[1],data[2],data[3])
        # t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO blog_duizhao (宠物编号,宠物名字,宠物价值,加入时间) VALUES ('%s','%s','%s','%s')" % (
            data[0], data[1], data[2],data[3])
        c.execute(sql)
        conn.commit()
        # break
    conn.close()


def get_buy():
    conn = sqlite3.connect('db.sqlite3')  # 链接数据库
    c = conn.cursor()
    datas = c.execute("SELECT 账号编号 FROM blog_shujuku WHERE 已卖='是'")

    for data in datas:
        print(data[0])
        with open('已卖.txt', 'a+') as ff:
            ff.write(data[0]+'\n')
    conn.close()

def get_pad():
    with open('已卖.txt','r') as f:
        # print(f.readlines())
        for i in f.readlines():
            d='D:\\0项目\job\PAD/'+i.strip('\n')
            # print(d)
            if os.path.isfile(d):
                print('删除'+d)
                os.remove(d)
    qd=os.listdir('D:\\0项目\job\PAD/')
    os.remove('清单.txt')
    with open('清单.txt','w') as f:
        for i in qd:
            print(i)
            f.write(i+'\n')


def get_qd():#获取清单
    qd=os.listdir('D:\\0项目\job\PAD/')
    with open('清单.txt','w') as f:
        for i in qd:
            print(i)
            f.write(i+'\n')


#更新数据
# upshuju()
#清除已卖或者被封
# isbuy()

# copyshuju()
# copyduizhao()
get_buy()
<<<<<<< HEAD
# get_pad()
=======
# get_pad()
>>>>>>> aec4e9307ad4caece324de86baee55c1dbe17b63
