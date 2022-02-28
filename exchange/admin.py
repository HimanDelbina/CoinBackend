from django.contrib import admin
from .models import ExchangeModel


class ExchangeAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'site', 'rank']
    list_display = ['pk', 'title', 'description', 'site', 'rank']
    search_fields = ['title', 'description', 'site', 'rank']
    list_filter = ['title', 'description', 'site', 'rank']


admin.site.register(ExchangeModel, ExchangeAdmin)
