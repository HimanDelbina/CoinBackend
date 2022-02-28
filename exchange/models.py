from distutils import text_file
from turtle import title
from django.db import models

# Create your models here.


class ExchangeModel(models.Model):
    title = models.CharField(max_length=50,verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    site = models.CharField(max_length=100,verbose_name='سابت')
    rank = models.IntegerField(verbose_name='رتبه')

    class Meta:
        verbose_name_plural = "صرافی ها"
        verbose_name = 'صرافی'

    def __str__(self):
        return self.title
