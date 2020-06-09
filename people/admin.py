from django.contrib import admin
from .models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    """设置列表可显示的字段"""
    list_display = ('name', 'age',)

    '''设置过滤选项'''
    list_filter = ('name', 'age',)

    '''每页显示条目数'''
    list_per_page = 5

    '''设置可编辑字段'''
    list_editable = ('age',)

    '''按日期月份筛选'''
    # date_hierarchy = 'age'

    '''按发布日期排序'''
    ordering = ('-age',)


admin.site.register(Person, PersonAdmin)

# 修改网页title和站点header。
admin.site.site_title = "管理台"
admin.site.site_header = "管理后台"
