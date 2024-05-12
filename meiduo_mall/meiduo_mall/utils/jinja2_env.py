from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,#重定向路由
    })
    return env


"""
确保可以使用模板引擎中的{{ url('路由命名空间') }} {{ static('静态文件相对路径') }}这类语句 
"""