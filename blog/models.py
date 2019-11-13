from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Hot(models.Model):
    #热门宠物
    name = models.CharField(max_length=100)
