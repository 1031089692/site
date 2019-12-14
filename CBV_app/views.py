from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View


class Login(View):

    def get(self, request):
        return HttpResponse("ok")