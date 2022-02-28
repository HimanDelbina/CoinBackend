from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# class AccessLevel(models.Model):
#     title = models.CharField(max_length=100, unique=True,
#                              blank=True, null=True, verbose_name='عنوان')
#     description = models.TextField(
#         verbose_name='توضیحات', blank=True, null=True,)

#     class Meta:
#         verbose_name_plural = "سطح های دسترسی"
#         verbose_name = 'سطح دسترسی'

#     def __str__(self):
#         return self.title


# class AccessLevelGroup(models.Model):
#     title = models.CharField(max_length=100, unique=True,
#                              blank=True, null=True, verbose_name='عنوان')
#     description = models.TextField(
#         verbose_name='توضیحات', blank=True, null=True,)
#     access_level = models.ManyToManyField(
#         AccessLevel, null=True, blank=True, verbose_name="سطح دسترسی")

#     class Meta:
#         verbose_name_plural = "گروه های سطح دسترسی"
#         verbose_name = 'گروه سطح دسترسی'

#     def __str__(self):
#         return self.title


# class UserAccessLevelGroup(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, blank=True,)
#     access_level_group = models.ForeignKey(
#         AccessLevelGroup, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="گروه سطح دسترسی")

#     class Meta:
#         verbose_name_plural = "سطح دسترسی کاربرها"
#         verbose_name = 'سطح دسترسی کاربر'

#     def __str__(self):
#         return str(self.user.first_name) + ' ' + str(self.user.last_name)


class Role(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True,)
    description = models.TextField(
        verbose_name='توضیحات', blank=True, null=True,)

    class Meta:
        verbose_name_plural = "نقش ها"
        verbose_name = 'نقش'

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, verbose_name="نقش")
    phone_number = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="شماره موبایل")
    fcm_token = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="توکن فایربیس")

    class Meta:
        verbose_name_plural = "پروفایل ها"
        verbose_name = 'پروفایل'

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            print("******** profile created ********")
            Profile.objects.create(user=instance)
    except:
        pass


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        print("******** instance saved ********")
        instance.profile.save()
    except:
        pass
