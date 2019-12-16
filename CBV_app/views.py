from django.shortcuts import render, HttpResponse
from test_app.models import *
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
import json
import random
import re
# Create your views here.

from django.views import View


class Login(View):

    def get(self, request):
        return HttpResponse("ok")


class Starter(View):
    def get(self, request):
        return render(request, 'base.html')


class Order_list(View):
    def get(self, request):
        order_list = Order.objects.all()
        paginator = Paginator(order_list, 10)
        order_list = Order.objects.all()
        paginator = Paginator(order_list, 10)
        try:
            current_page_num = request.GET.get("page", 1)  # 当前页码数,取值取不到默认为1。
            current_page = paginator.page(current_page_num)  # 当前页对象
        except EmptyPage as e:
            current_page_num = 1
            current_page = paginator.page(1)
        var = (int(current_page_num) - 1) * 10
        return render(request, 'order_list.html', {'current_page': current_page,
                                              "paginator": paginator,
                                              "current_page_num": int(current_page_num),
                                              "var": var
                                              })
