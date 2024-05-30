from django.contrib import admin
from django.urls import path, include,re_path

# from django.conf.urls import url#现在已经废弃掉了这个url包
# from django.urls import re_path


# 从views.py中导入RegisterView类
# from .views import RegisterView
from . import views

urlpatterns = [
    
    # 首页广告
    re_path(r'^$', views.IndexView.as_view(), name='index'),#http://127.0.0.1:8000/就可以访问
]