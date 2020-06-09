from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import hashlib

# Create your views here.
from django.urls import reverse

from rbac import models
from rbac.models import User
from rbac.models import UserForm, RegisterForm


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('../index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return render(request, 'index.html')
                else:
                    message = "密码不正确!"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         message = "所有字段都必须填写！"
#         if username and password:  # 确保用户名和密码都不为空
#             username = username.strip()
#             # 用户名字符合法性验证
#             # 密码长度验证
#             # 更多的其它验证.....
#             try:
#                 user = models.User.objects.get(name=username)
#                 if user.password == password:
#                     return render(request, 'index.html',)
#                 else:
#                     message = "密码不正确！"
#             except:
#                 message = "用户不存在！"
#         return render(request, 'login.html', {"message": message})
#     return render(request, 'login.html', )


def register(request):
    if request.session.get('is_login', None):
    # 登录状态不允许注册。你可以修改这条原则！
        return redirect('/rbac/index')

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不同!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户已经存在，请重新选择用户名！"
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱地址已被注册,请使用别的邮箱!"
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('../login/')

    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect('/rbac/index/')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/rbac/index/")


def base(request):
    return render(request, 'base.html', )


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def test(request):
    return render(request, 'test.html', locals())
    # return HttpResponse('test')