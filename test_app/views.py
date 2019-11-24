from django.shortcuts import render, HttpResponse, redirect
from test_app.models import *
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
# Create your views here.
import json
import time
import random


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
    """造数据(开始之前关闭验证中间件)
    order_list = []
    a = random.randint(1, 4)
    b = random.randint(1, 3)
    c = random.randint(1, 3)
    for i in range(100):
        order = Order(order_num="CN_%s" % i,
                      price=i*i,
                      pay_date=time.strftime('2019-11-22 00:00:00.000000'),
                      order_status=a,
                      customer_id=b,
                      food=c
                      )
        order_list.append(order)
    Order.objects.bulk_create(order_list)
    return HttpResponse('OK')
    """
    order_list = Order.objects.all()
    paginator = Paginator(order_list, 10)
    try:
        current_page_num = request.GET.get("page", 1)  # 当前页码数,取值取不到默认为1。
        current_page = paginator.page(current_page_num)  # 当前页对象
    except EmptyPage as e:
        current_page_num = 1
        current_page = paginator.page(1)
    return render(request, 'index.html', {'current_page': current_page,
                                          "paginator": paginator,
                                          "current_page_num": int(current_page_num),
                                          })


def del_order(request, delete_order_id):
    # 表单删除订单
    Order.objects.filter(oid=delete_order_id).delete()
    return redirect(reverse('shouye'))


def edit_order(request,edit_order_id):
    # 表单编辑订单
    if request.method == 'GET':
        order = Order.objects.filter(oid=edit_order_id)[0]
        return render(request, 'edit_order.html', {'order': order})
    else:
        order_num = request.POST.get("order_num")
        price = request.POST.get("price")
        pay_date = request.POST.get("pay_date")
        order_status = request.POST.get("order_status")
        Order.objects.filter(oid=edit_order_id).update(order_num=order_num, price=price, pay_date=pay_date,
                                                       order_status=order_status)


def add_order(request):
    if request.method == 'POST':
        data = request.POST.dict()   # 默认的QuerySet类型不可改，需转成字典操作。
        del data['csrfmiddlewaretoken']  # 去除多余的选项
        order = Order.objects.create(**data)
        return redirect(reverse('shouye'))
    else:
        return render(request, 'add_order.html')


def del_ajax_order(request,del_id):
    response = {"code": 200, "data": "删除成功"}
    try:
        Order.objects.filter(pk=del_id).delete()
        return HttpResponse(json.dumps(response))
    except Exception as e:
        print(e)
        response["code"] = 0
        response["data"] = "删除失败"
        return HttpResponse(json.dumps(response))


def error(request):
    return render(request, "error.html")
