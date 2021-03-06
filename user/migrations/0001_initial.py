# Generated by Django 3.2.8 on 2022-01-19 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'سطح دسترسی',
                'verbose_name_plural': 'سطح های دسترسی',
            },
        ),
        migrations.CreateModel(
            name='AccessLevelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('access_level', models.ManyToManyField(blank=True, null=True, to='user.AccessLevel', verbose_name='سطح دسترسی')),
            ],
            options={
                'verbose_name': 'گروه سطح دسترسی',
                'verbose_name_plural': 'گروه های سطح دسترسی',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'نقش',
                'verbose_name_plural': 'نقش ها',
            },
        ),
        migrations.CreateModel(
            name='UserAccessLevelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.accesslevelgroup', verbose_name='گروه سطح دسترسی')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سطح دسترسی کاربر',
                'verbose_name_plural': 'سطح دسترسی کاربرها',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('fcm_token', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.role', verbose_name='نقش')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
    ]
