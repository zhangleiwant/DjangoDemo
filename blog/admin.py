from django.contrib import admin
from . import models


# Register your models here.

# admin技巧 显示详细内容  添加时间过滤器
class ArticleAdmin(admin.ModelAdmin):
    # 显示详细内容
    list_display = ('title', 'content', 'pub_time')
    #     添加时间过滤器 元祖只有一个元素的话必须加逗号
    list_filter = ('pub_time',)


# 关联到后台
admin.site.register(models.Article, ArticleAdmin)
