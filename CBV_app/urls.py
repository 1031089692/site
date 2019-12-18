# coding:utf-8

from django.contrib import admin
from django.urls import path,re_path
from CBV_app import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('starter/', views.Starter.as_view()),
    path('get_customer/', views.get_customer),
    path('post_customer/', views.post_customer),
    path('base/', views.base),
    path('sytzlist/', views.sytzlist),
    path('test/', views.test),
]