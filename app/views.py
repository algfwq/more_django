from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.core import mail

# Create your views here.
def set(request):
    cache.set('message', '奥利给！', 120)
    return HttpResponse('已经储存缓存')

def get(request):
    return HttpResponse(cache.get('message'))

def send_email(request):
    mail.send_mail(
        subject='Windows10对你妈妈的问候！',  # 题目
        message='操你妈！',  # 消息内容
        from_email='algpythontest@outlook.com',  # 发送者[当前配置邮箱]
        recipient_list=['3104374883@qq.com'],  # 接收者邮件列表
        auth_password='ss699610'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
    )
    return HttpResponse('OK')

