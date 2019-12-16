# coding:utf-8

from django.contrib import admin
from django.urls import path,re_path
from CBV_app import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('starter/', views.Starter.as_view()),
    path('order_list/', views.Order_list.as_view()),
]