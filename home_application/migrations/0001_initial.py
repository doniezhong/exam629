# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_name', models.CharField(max_length=20)),
                ('update_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('bk_biz_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=10)),
                ('admin', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('exam_time', models.DateTimeField()),
                ('site', models.CharField(max_length=20)),
                ('content', models.FileField(upload_to=b'/uploads')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_name', models.CharField(max_length=20)),
                ('update_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('department', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
                ('res', models.CharField(max_length=10)),
                ('mark', models.CharField(max_length=80)),
                ('exam_id', models.ForeignKey(to='home_application.Exam')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
