from django.test import TestCase

# Create your tests here.


# def add():
#     a = 1
#
#     def inner():
#         print(a)
#     return inner
#
#
# a = add()
# print(a.__closure__)


def login(func):

    def inner():
        print("aaaaaaaaaa")
        func()
    return inner


@login
def index():
    print("hello")


index()