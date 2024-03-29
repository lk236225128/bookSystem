# Generated by Django 2.2.7 on 2019-11-21 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=20, verbose_name='书名')),
                ('authorName', models.CharField(max_length=20, verbose_name='作者')),
                ('introduction', models.CharField(max_length=20, verbose_name='简介')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.CharField(max_length=20, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '图书信息表',
                'verbose_name_plural': '图书信息表',
            },
        ),
    ]
