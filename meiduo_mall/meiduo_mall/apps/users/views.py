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

# 自定义的包
from users.models import User
from meiduo_mall.utils.response_code import RETCODE
# Create your views here.
class MobileCountView(View):
    """判断手机号是否重复注册"""
# 像这种带参数的请求都是顺延的
    def get(self, request, mobile):
        """
        :param mobile: 手机号
        :return: JSON
        """
        count = User.objects.filter(mobile=mobile).count()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'count': count})
class UsernameCountView(View):
    """判断用户名是否重复注册"""
# 像这种带参数的请求都是顺延的
    def get(self, request, username):
        """
        :param username: 用户名
        :return: JSON
        """
        # 实现主体业务逻辑：使用username查询对应的记录的条数(filter返回的是满足条件的结果集)   
        count = User.objects.filter(username=username).count()
        # 响应结果  状态码  错误提示信息  count值
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'count': count})

class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        request是本次请求的报文信息
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html')
    def post(self, request):
        """
        实现用户注册
        :param request: 请求对象
        :return: 注册结果
        """
        """实现用户注册业务逻辑"""
        # 接收参数：表单参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        sms_code_client = request.POST.get('sms_code')
        allow = request.POST.get('allow')
        print(username,password,password2,mobile,sms_code_client,allow)
        # 校验参数：前后端的校验需要分开，避免恶意用户越过前端逻辑发请求，要保证后端的安全，前后端的校验逻辑相同  前端校验逻辑在register.js中
        # 后端校验在这里
        # 判断参数是否齐全:all([列表])：会去校验列表中的元素是否为空，只要有一个为空，返回false
        if not all([username, password, password2, mobile, allow]):
            return http.HttpResponseForbidden('缺少必传参数')
        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return http.HttpResponseForbidden('请输入5-20个字符的用户名')
        # 判断密码是否是8-20个数字
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        # 判断两次密码是否一致
        if password != password2:
            return http.HttpResponseForbidden('两次输入的密码不一致')
        # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')
        
        
        # 判断短信验证码是否输入正确  先不管
        # redis_conn = get_redis_connection('verify_code')
        # sms_code_server = redis_conn.get('sms_%s' % mobile)
        # if sms_code_server is None:
        #     return render(request, 'register.html', {'sms_code_errmsg': '短信验证码已失效'})
        # if sms_code_client != sms_code_server.decode():
        #     return render(request, 'register.html', {'sms_code_errmsg': '输入短信验证码有误'})
        # 判断是否勾选用户协议
        if allow != 'on':
            return http.HttpResponseForbidden('请勾选用户协议')

        # 保存注册数据：是注册业务的核心 这里会自动给密码加密  然后放入到数据库
        # return render(request, 'register.html', {'register_errmsg': '注册失败'})
        print('校验成功!')
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return render(request, 'register.html', {'register_errmsg':'注册失败'})#页面展示出来

        # return http.HttpResponse('注册成功, 重定向到首页')
    
    # 下面这些代码先注释
        # 实现状态保持  里面已经将session写好了  
        login(request, user)

        # 响应结果:重定向到首页
        response = redirect(reverse('contents:index'))#重定向到index.html页面  contents是总路由的命名空间  index是子路由的命名空间

        # 为了实现在首页的右上角展示用户名信息，我们需要将用户名缓存到cookie中
        # response.set_cookie('key', 'val', 'expiry')
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)#设置cookie值存在时间15天  可以在127.0.0.1:8000中的请求头中找到cookie里面有username

        # 响应结果:重定向到首页
        return response