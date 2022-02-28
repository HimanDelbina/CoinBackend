from django.contrib import admin
from .models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image',
              'persiandate', 'persiantime', 'source']
    list_display = ['pk', 'title', 'description',
                    'image', 'persiandate', 'persiantime', 'source']
    search_fields = ['title', 'description', 'image',
                     'persiandate', 'persiantime', 'source']
    list_filter = ['title', 'description', 'image',
                   'persiandate', 'persiantime', 'source']


admin.site.register(NewsModel, NewsAdmin)
