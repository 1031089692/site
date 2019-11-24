"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from test_app import views

urlpatterns = [
    path('', views.index),   # 不知道为啥不能直接跳到index，这里加个path，临时解决方案
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index, name='shouye'),
    path('error/', views.error),
    re_path('del_order/(\d+)', views.del_order, name='shanchu'),
    re_path('edit_order/(\d+)', views.edit_order, name='bianji'),
    path('add_order/', views.add_order, name='zengjia'),
    re_path('del_ajax_order/(\d+)', views.del_ajax_order)
]
