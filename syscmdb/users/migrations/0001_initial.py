# Generated by Django 2.2.28 on 2023-05-16 16:14

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cn', models.CharField(max_length=50, verbose_name='中文名')),
                ('wechat', models.CharField(max_length=50, verbose_name='微信')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('info', models.TextField(verbose_name='备注')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
