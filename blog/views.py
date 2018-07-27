from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
# 定义响应函数
def call(request):
    return HttpResponse("我是一只小小鸟")


# templates 模板 命名不能写错 去查找html文件时候 根据 settings的注册的app模块中的html。找到第一个就用第一个。
# 在templates下多创建一个 与app重名的目录 将html放进去。
def ren(request):
    # pk = 相当于primary key  select条件
    articles = models.Article.objects.all()
    return render(request, 'blog/index1.html', {'articles': articles})


#博客详情
def detail(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})
