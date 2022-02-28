from turtle import title
from django.db import models
import os

from django.utils.html import mark_safe

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def news_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"news/{final_name}"
    return x


class NewsModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='خبر')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(
        null=True, upload_to=news_image_path, verbose_name='تصویر')
    persiandate = models.CharField(max_length=20, verbose_name='تاریخ فارسی')
    persiantime = models.CharField(max_length=20, verbose_name='ساعت فارسی')
    source = models.CharField(max_length=50, verbose_name='منبع خبر')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "اخبار ها"
        verbose_name = 'اخبار'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
