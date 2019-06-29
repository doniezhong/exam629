# -*- coding: utf-8 -*-
from django.db import models


class BaseOperateModel(models.Model):

    create_name = models.CharField(max_length=20)
    update_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def to_dic(self):
        result_dict = dict([(f.name, getattr(self, f.name)) for f in self._meta.fields])
        return result_dict

    class Meta:
        abstract = True


class Exam(BaseOperateModel):
    bk_biz_id = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    admin = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    exam_time = models.DateTimeField()
    site = models.CharField(max_length=20)
    content = models.FileField(upload_to='/uploads')


class Student(BaseOperateModel):
    exam_id = models.ForeignKey(Exam)
    department = models.CharField(max_length=20)
    score = models.IntegerField()
    res = models.CharField(max_length=10)
    mark = models.CharField(max_length=80)
