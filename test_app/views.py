from django.shortcuts import render, HttpResponse, redirect
from test_app.models import *
from django.urls import reverse
# Create your views here.
import time


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        res = {"user": None, "data": None}
        # print(request.POST)
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd).first()
        import json
        if user_obj:
            res["user"] = user
            res["data"] = "登录成功"
            request.session["name"] = user
            request.session["login"] = True
            return HttpResponse(json.dumps(res))
        else:
            res["data"] = "账号或者密码错误"
            return HttpResponse(json.dumps(res))
    else:
        pass


def index(request):
    return render(request, "index.html")


def test_01(request):
    return HttpResponse("ok")


def error(request):
    return render(request, "error.html")
