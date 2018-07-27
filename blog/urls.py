from django.urls import path
from . import views

# 'Specifying a namespace in include() without providing an app_name '
# 困扰的问题 python3需要在这里添加 Appname
app_name = 'blog'
urlpatterns = [
    path('call/', views.call),
    path('', views.ren),
    # 正则表达式
    # python2版本 url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # url(r'^detail/(?P<article_id>[0-9]+)$')
    # python3版本  注意后面加反斜杠
    path('detail/<int:article_id>/', views.detail, name='article_detail')
]
