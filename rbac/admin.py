from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """设置列表可显示的字段"""
    list_display = ('name', 'sex', 'email', 'c_time')

    '''设置过滤选项'''
    list_filter = ('name', 'sex',)

    '''每页显示条目数'''
    list_per_page = 51

    '''设置可编辑字段'''
    list_editable = ('sex',)

    '''按日期月份筛选'''
    # date_hierarchy = 'age'

    '''按发布日期排序'''
    ordering = ('-c_time',)


admin.site.register(User, UserAdmin)