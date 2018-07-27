from django.urls import path
from . import views

urlpatterns = [
    path('call/', views.call),
    path('ren/', views.ren),
    # 正则表达式
    # python2版本 url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # url(r'^detail/(?P<article_id>[0-9]+)$')
    # python3版本  注意后面加反斜杠
    path('detail/<int:article_id>/', views.detail)
]
