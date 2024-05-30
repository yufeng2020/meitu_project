from django.contrib import admin
from django.urls import path, include,re_path

# from django.conf.urls import url#现在已经废弃掉了这个url包
# from django.urls import re_path


# 从views.py中导入RegisterView类
# from .views import RegisterView
from . import views

urlpatterns = [
    # 每一个子路由都对应一个views.py中的函数
    # re_path(r'^register/$', views.RegisterView.as_view(), ),#用户在url中输入register/就能匹配到注册页面
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 判断用户名是否重复注册   不需要做命名空间 因为不需要重定向到某个页面
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$', views.UsernameCountView.as_view()),
    # 判断手机号是否重复注册
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
]