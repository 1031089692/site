from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class AccessFrequencyVerification(models.Model):
    ip = models.CharField(max_length=32)
    Access_time = models.DateTimeField(verbose_name='访问时间')
    Number_visits = models.IntegerField(verbose_name='访问次数')
