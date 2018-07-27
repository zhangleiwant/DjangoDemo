from django.contrib import admin
from . import models
# Register your models here.

#关联到后台
admin.site.register(models.Article)