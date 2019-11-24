# coding:utf-8
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render, HttpResponse
from test_app.models import *
from django.utils import timezone
import datetime


class SessionCheck(MiddlewareMixin):
    """
    做session校验，除login接口。
    其余接口没有session的一律重定向到login
    """
    def process_request(self, request):
        if request.path in ["/login/"]:
            return None
        else:
            slogin = request.session.get("login")
            if not slogin:
                return redirect("/login/")
            elif request.path in ["/error/"]:
                return None
            else:
                return None

    def process_response(self, request, response):
        return response


class AccessFrequencyVerification2(MiddlewareMixin):
    """
    做访问频率校验。
    1、每次登录。在表里面查询有无该ip的访问记录。
    2、如果没有。记录ip、访问时间。 访问次数写成1
    3、如果表里面查询有该IP的访问记录。且访问时间距当前时间小于60s，则访问次数+1。大于则不变。
    4、访问之前判断次数有没有大于20。如果大于，请求接到一个独立页面。
    """
    def process_request(self, request):
        if request.path in ["/error/"]:
            return None
        else:
            if request.META.get('HTTP_X_FORWARDED_FOR'):
                ip = request.META.get("HTTP_X_FORWARDED_FOR")
            else:
                ip = request.META.get("REMOTE_ADDR")

            a = AccessFrequencyVerification.objects.filter(ip=ip).first()
            if a is None:
                # 新用户插入数据逻辑
                time = timezone.now()
                AccessFrequencyVerification.objects.create(
                    ip=ip,
                    Access_time=time,
                    Number_visits=1,
                )
            else:
                # 老用户处理逻辑
                Access_time = AccessFrequencyVerification.objects.filter(ip=ip).first().Access_time
                time = timezone.now()
                time_difference = time-Access_time
                a = AccessFrequencyVerification.objects.filter(ip=ip).first().Number_visits
                b = datetime.timedelta(seconds=60)
                if time_difference < b:
                    # 60s之内连续登录
                    AccessFrequencyVerification.objects.filter(ip=ip).update(Number_visits=a+1)
                else:
                    # 60s之后登录
                    AccessFrequencyVerification.objects.filter(ip=ip).update(Access_time=time)
                if a > 200:
                    return redirect("/error/")
                else:
                    return None






