from django.db import models

# Create your models here.

# 在这里定义用户模型类
from django.contrib.auth.models import AbstractUser


# 此外在django中框架里面就设计了username不能重复
class User(AbstractUser):
    """自定义用户模型类的手机号字段  默认最大手机号长度11位   unique每个手机号码不重复   verbose_name是默认给出的解释"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

# 使用元类自定义表的名字
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name#也是“用户”

    def __str__(self):
        return self.username