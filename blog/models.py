from django.db import models


# Create your models here.
# 该文件 操作数据库 ORM  对象关系映射 创建的类对应数据库表
class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)
    #默认对象 改为对象属性 3.0之后
    def __str__(self):
        return self.title