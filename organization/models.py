# _*_ encoding:utf-8 _*_
# python自带的一些包
from __future__ import unicode_literals
from datetime import datetime

# 第三方包
from django.db import models


# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'封面图')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    work_year = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    point = models.CharField(max_length=50, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
