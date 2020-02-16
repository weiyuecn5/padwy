from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(default = timezone.now)
    modified_time = models.DateTimeField(auto_now = True)


class Hot(models.Model):
    name = models.CharField(max_length=100)
    number=models.CharField(max_length=50,default=0)

class shujuku(models.Model):
    账号编号=models.CharField(max_length=100,primary_key=True)
    石头数量=models.IntegerField (blank=True,default=0) #修改数据类型
    等级=models.CharField(max_length=100,blank=True)
    更新时间=models.CharField(max_length=100,blank=True)
    宠物=models.TextField()
    已卖=models.CharField(max_length=20,default='否')
    买家=models.CharField(max_length=100,blank=True)
    价格=models.CharField(max_length=100,blank=True)

class duizhao(models.Model):
    宠物编号=models.CharField(max_length=100,primary_key=True)
    宠物名字=models.CharField(max_length=100,blank=True)
    宠物价值 = models.CharField(max_length=100, blank=True)
    加入时间=models.DateTimeField(default = timezone.now)
