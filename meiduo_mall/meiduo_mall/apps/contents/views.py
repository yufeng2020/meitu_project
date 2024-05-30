from django_redis import get_redis_connection
# 从django的view视图中导入View视图
from django.views import View
from django import http

from django.shortcuts import render, redirect
from django import http
import re, json, logging
from django.db import DatabaseError
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django_redis import get_redis_connection
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# Create your views here.
class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页广告界面"""
        return render(request, 'index.html')#http://127.0.0.1:8000/就可以访问