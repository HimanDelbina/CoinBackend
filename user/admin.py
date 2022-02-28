from django.contrib import admin
from .models import Role, Profile


class RoleAdmin(admin.ModelAdmin):
    fields = ['title', 'description', ]
    list_display = ['pk', 'title', 'description', ]
    search_fields = ['title', 'description', ]
    list_filter = ['title', 'description', ]


class ProfileAdmin(admin.ModelAdmin):
    fields = ["user", "role", "phone_number", "fcm_token"]
    list_display = ['pk', "user",
                    "role", "phone_number", "fcm_token"]
    search_fields = ["user",  "phone_number", "fcm_token"]
    list_filter = []


# class AccessLevelAdmin(admin.ModelAdmin):
#     fields = ["title", "description"]
#     list_display = ["title", "description"]
#     search_fields = ["title", "description"]
#     list_filter = ["title", "description"]


# class AccessLevelGroupAdmin(admin.ModelAdmin):
#     fields = ["title", "access_level", "description"]
#     list_display = ["title", "access_levels", "description"]
#     search_fields = ["title", "description"]
#     list_filter = ["title", "description"]

#     def access_levels(self, obj):
#         return [o.title for o in obj.access_level.all()]


# class UserAccessLevelGroupAdmin(admin.ModelAdmin):
#     fields = ["user", "access_level_group"]
#     list_display = ["user", "access_level_group"]
#     search_fields = ["user", "access_level_group"]
#     list_filter = ["user", "access_level_group"]


admin.site.register(Role, RoleAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(AccessLevel, AccessLevelAdmin)
# admin.site.register(AccessLevelGroup, AccessLevelGroupAdmin)
# admin.site.register(UserAccessLevelGroup, UserAccessLevelGroupAdmin)
