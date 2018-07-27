from django.urls import path
from . import views

app_name = 'blog_tools'
urlpatterns = [
    path('call/', views.call),
    path('ren/', views.ren),
]
