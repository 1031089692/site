from django.db import models

# Create your models here.


class UserInfo(models.Model):
    # 用户信息表
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    r_pwd = models.CharField(max_length=32)

    def __str__(self):
        return "{} : {}".format(self.user, self.pwd)


class AccessFrequencyVerification(models.Model):
    # 用户访问频率表
    ip = models.CharField(max_length=32)
    Access_time = models.DateTimeField(verbose_name='访问时间')
    Number_visits = models.IntegerField(verbose_name='访问次数')


class Order(models.Model):
    # 用户订单表
    oid = models.AutoField(primary_key=True, verbose_name='编号',)    # AutoField 自增
    order_num = models.CharField(max_length=32, verbose_name='订单号')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='实付金额')  # DecimalFiel 高精度浮点 第一个
    # 参数表示总位数，第二个表示小数位
    pay_date = models.DateTimeField(verbose_name='付款日期')    # DateTimeField 日期
    order_status = models.CharField(max_length=32, verbose_name='订单状态: 1、进行中。3已结束 2、备用状态')
    customer = models.ForeignKey(to='Customer', db_constraint=False, on_delete=models.DO_NOTHING)
    food = models.CharField(max_length=256, verbose_name='订单食物')
    fooddetails =models.ManyToManyField(to='FoodDetails',)


class OrderReplyRecord(models.Model):
    # 订单评价
    oid = models.AutoField(primary_key=True)
    order_num = models.CharField(max_length=32, verbose_name='订单号')
    order_evaluate = models.CharField(max_length=256, verbose_name='订单评价')
    reply_record = models.CharField(max_length=256, verbose_name='订单回评')
    evaluate_date = models.DateTimeField(verbose_name='评价时间')
    reply_record_date = models.DateTimeField(verbose_name='回评时间')


class Customer(models.Model):
    # 订单顾客表
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='顾客姓名')
    address = models.CharField(max_length=32, verbose_name='地址')
    phone_number = models.CharField(max_length=32, verbose_name='电话')


class FoodDetails(models.Model):
    # 食物热量查询表
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='食物名称')
    calories = models.IntegerField(verbose_name='食品热量/卡路里')
