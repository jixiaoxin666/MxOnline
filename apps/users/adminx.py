# _*_ encoding:utf-8 _*_
__author__ = 'jihuixin'
__date__ = '2018/3/15 下午5:32'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True  # 使用主题功能
    use_bootswatch = True


# 设置xadmin的左上角页头和下面的页脚,如下两个参数是固定的
class GlobalSetting(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'  # 设置左侧菜单的显示方式(可折叠可收起)


class EmailVerifyRecordAdmin(object):
    # 定义后台列表显示列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行
    search_fields = ['code', 'email', 'send_type']
    # 过滤功能
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 定义后台列表显示列
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 搜索功能 定义后台在做搜索时在哪些字段中进行 注:时间不能作为搜索条件
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# model和admin进行关联注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)  # 把xadmin的主题功能注册进来
xadmin.site.register(views.CommAdminView, GlobalSetting)  # 把xadmin的页头和页脚的设置功能注册进来
