from django.db import models

# Create your models here.


class WallModel(models.Model):
    englishname = models.CharField(
        max_length=100, verbose_name='نام ارز انگلیسی')
    persianame = models.CharField(max_length=100, verbose_name='نام ارز فارسی')
    coinnumber = models.CharField(max_length=100, verbose_name='تعداد ارز')
    sender = models.CharField(max_length=100, verbose_name='فرستنده')
    reciver = models.CharField(max_length=100, verbose_name='گیرنده')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "خرید نهنگ ها"
        verbose_name = 'خرید نهنگ'

    def __str__(self):
        return self.persianame
