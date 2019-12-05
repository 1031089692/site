from django.shortcuts import render, HttpResponse, redirect
from test_app.models import *
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.forms import widgets
from django.core.exceptions import ValidationError
from django import forms
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.http import JsonResponse
# Create your views here.
import json
import random
import re


class UserForm(forms.Form):
    msg = {"required": "该字段不能为空"}
    user = forms.CharField(min_length=5, label="用户名", error_messages=msg, )
    pwd = forms.CharField(label="密码", error_messages=msg, widget=widgets.PasswordInput())
    r_pwd = forms.CharField(label="再次输入密码", error_messages=msg, widget=widgets.PasswordInput())
    email = forms.EmailField(label="邮箱", error_messages={"invalid": "邮箱格式错误"},)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({"class": "form-control"})

    def clean_user(self):
        val = self.cleaned_data.get("user")
        ret = UserInfo.objects.filter(user=val).first()
        if not ret:
            return val
        else:
            raise ValidationError("用户名已存在！")

    def clean_pwd(self):
        val = self.cleaned_data.get("pwd")
        if val.isdigit():
            raise ValidationError("密码不能是纯数字v")
        else:
            return val

    def clean_email(self):
        val = self.cleaned_data.get("email")
        if re.search('\\w[-\\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\\.)+[A-Za-z]{2,14}', val):   # 凡是\都换成\\
            return val
        else:
            raise ValidationError("邮箱格式错误")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        r_pwd = self.cleaned_data.get("r_pwd")

        if pwd and r_pwd and pwd != r_pwd:
            self.add_error("r_pwd", ValidationError("两次密码输入不一致"))
        else:
            return self.cleaned_data


def reg(request):
    if request.method == 'GET':
        form = UserForm()       # 通过form标签渲染html
        return render(request, "form_reg.html", locals())
    else:
        form = UserForm(request.POST)    # 数据校验
        if form.is_valid():
            UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse("ok")
        else:
            errors = form.errors
            if form.errors.get("__all__"):
                g_error = form.errors.get("__all__")[0]
            return render(request, "form_reg.html", locals())


def ajax_reg(request):
    if request.method == 'GET':
        form = UserForm()       # 通过form标签渲染html
        return render(request, "ajax_reg.html", locals())
    elif request.method == 'POST':
        try:
            res = {"user": None, "data": ""}
            form = UserForm(request.POST)
            if form.is_valid():
                UserInfo.objects.create(**form.cleaned_data)
                res["user"] = form.cleaned_data.get("user")
                res["data"] = "成功"
            else:
                res["data"] = form.errors
            return HttpResponse(json.dumps(res))
        except Exception as e:
            return e
    else:
        pass


def get_random_color():
    a = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)
    return a


def get_valid_img(request):
    img = Image.new("RGB", (350, 35), get_random_color())   # 自动生成图
    draw = ImageDraw.Draw(img)     # 插入画笔
    font = ImageFont.truetype("static/font/fullhouse.ttf", 32)   # 引入字体及大小
    keep_str = ""
    for i in range(6):  # 随机字符串
        random_num = str(random.randint(0, 9))
        random_lowalf = chr(random.randint(97, 122))
        random_upperalf = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_lowalf, random_upperalf])
        draw.text((i*30+80, 0), random_char, get_random_color(), font=font)
        keep_str += random_char
        request.session['keep_str'] = keep_str
    width = 350
    height = 35
    # 加噪线
    for i in range(10):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())
    # 加噪点
    for i in range(10):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x+4, y+4,), 0, 90, fill=get_random_color())
    # 内容写入内存
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    return HttpResponse(data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        res = {"user": None, "data": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        validcode = request.POST.get("validcode")
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd).first()
        import json
        if validcode.upper() != request.session.get("keep_str").upper():    # 不区分大小写。
            res["data"] = "验证码输入错误"
            return HttpResponse(json.dumps(res))
        elif user_obj:
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
    var = (int(current_page_num)-1)*10
    return render(request, 'index.html', {'current_page': current_page,
                                          "paginator": paginator,
                                          "current_page_num": int(current_page_num),
                                          "var": var
                                          })


def del_order(request, delete_order_id):
    # 表单删除订单
    Order.objects.filter(oid=delete_order_id).delete()
    return redirect(reverse('shouye'))


def edit_order(request, edit_order_id):
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
