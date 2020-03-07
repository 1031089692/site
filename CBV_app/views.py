from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from CBV_app.models import *
from django.core.paginator import Paginator, EmptyPage
from urllib import parse
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
from  django.db.models import Q
# Create your views here.

from django.views import View
from rest_framework.views import APIView
from rest_framework.request import Request


class Login(APIView):

    def get(self, request):
        self.dispatch()
        return HttpResponse("ok")

    def post(self, request):
        pass


class Starter(View):
    def get(self, request):
        return render(request, 'base.html')

    def post(self, request):
        pass


def get_customer(request):
    return render(request, "customer_list.html")


def post_customer(request):
    res = {"code": 200, "data": None}
    val = request.POST.get("content")
    customer_list = Customer.objects.values().all().order_by("id")
    if val:
        customer_list = customer_list.values().filter(Q(name__contains=val))
        customer_list = list(customer_list)
        res["data"] = customer_list
        return JsonResponse(res)
    else:
        customer_list = list(customer_list)
        res["data"] = customer_list
        return JsonResponse(res)


def test(request):
    return render(request, "test.html")


def base(request):
    return render(request, "base.html")


def sytzlist(request):
    res = {"code": 200, "data": "成功"}
    return HttpResponse(json.dumps(res))
