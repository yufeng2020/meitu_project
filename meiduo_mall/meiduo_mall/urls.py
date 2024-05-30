"""
URL configuration for meiduo_mall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# from django.conf.urls import url#现在已经废弃掉了这个url包
# from django.urls import re_path



urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # users总路由
    # re_path(r'^', include('users.urls')),#因此在users目录中要新建一个urls.py 并且在里面写东西
    re_path(r'^', include(('users.urls', 'users'), namespace='users')),#不能使用
    # contents的总路由
    re_path(r'^', include(('contents.urls', 'contents'), namespace='contents')),
]





