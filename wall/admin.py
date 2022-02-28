from django.contrib import admin

from wall.models import WallModel

# Register your models here.


class WallAdmin(admin.ModelAdmin):
    fields = ['englishname', 'persianame', 'coinnumber', 'sender',
              'reciver', ]
    list_display = ['pk', 'englishname', 'persianame', 'coinnumber', 'sender',
                    'reciver', ]
    search_fields = ['englishname', 'persianame', 'coinnumber', 'sender',
                     'reciver', ]
    list_filter = ['englishname', 'persianame', 'coinnumber', 'sender',
                   'reciver', ]


admin.site.register(WallModel, WallAdmin)
