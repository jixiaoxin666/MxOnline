# _*_ encoding:utf-8 _*_
__author__ = 'jihuixin'
__date__ = '2018/3/15 下午9:46'

import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    # 定义后台列表显示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行
    search_fields = ['desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']
    # 过滤功能
    list_filter = ['desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums']


class LessonAdmin(object):
    # 定义后台列表显示列
    list_display = ['course', 'name', 'add_time']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行
    search_fields = ['course__name', 'name']  # 外键需要指明外键表的字段(用双下划线)
    # 过滤功能
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    # 定义后台列表显示列
    list_display = ['lesson', 'name', 'add_time']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行
    search_fields = ['lesson__name', 'name']  # 外键需要指明外键表的字段(用双下划线)
    # 过滤功能
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 定义后台列表显示列
    list_display = ['course', 'name', 'download', 'add_time']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行
    search_fields = ['course__name', 'name', 'download']  # 外键需要指明外键表的字段(用双下划线)
    # 过滤功能
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
