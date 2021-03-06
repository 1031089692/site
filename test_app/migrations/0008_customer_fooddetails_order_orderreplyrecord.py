# Generated by Django 2.1.7 on 2019-11-24 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_auto_20191123_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='顾客姓名')),
                ('address', models.CharField(max_length=32, verbose_name='地址')),
                ('phone_number', models.CharField(max_length=32, verbose_name='电话')),
            ],
        ),
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='食物名称')),
                ('calories', models.IntegerField(verbose_name='食品热量/卡路里')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('order_num', models.CharField(max_length=32, verbose_name='订单号')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='实付金额')),
                ('pay_date', models.DateTimeField(verbose_name='付款日期')),
                ('order_status', models.CharField(max_length=32, verbose_name='订单状态: 1、进行中。3已结束 2、备用状态')),
                ('food', models.CharField(max_length=256, verbose_name='订单食物')),
                ('customer', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='test_app.Customer')),
                ('fooddetails', models.ManyToManyField(to='test_app.FoodDetails')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReplyRecord',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('order_num', models.CharField(max_length=32, verbose_name='订单号')),
                ('order_evaluate', models.CharField(max_length=256, verbose_name='订单评价')),
                ('reply_record', models.CharField(max_length=256, verbose_name='订单回评')),
                ('evaluate_date', models.DateTimeField(verbose_name='评价时间')),
                ('reply_record_date', models.DateTimeField(verbose_name='回评时间')),
            ],
        ),
    ]
