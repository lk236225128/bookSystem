# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    bookName=models.CharField(max_length=20,verbose_name=u"书名")
    authorName=models.CharField(max_length=20,verbose_name=u"作者")
    introduction=models.CharField(max_length=20,verbose_name=u"简介")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"图书信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bookName