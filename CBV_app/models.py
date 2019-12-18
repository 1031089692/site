from django.db import models
from multiselectfield import MultiSelectFormField
# Create your models here.


gender_choices = (("1", "男"),
                  ("2", "女"))
vip_grade_choices = (("1", "黄金会员"),
                     ("2", "白金会员"),
                     ("3", "钻石会员"),)
is_test_choices = (("1", "测试用户"),
                   ("0", "非测试用户"))


class Customer(models.Model):
    # 用户信息表
    name = models.CharField('用户姓名', max_length=32, null=True, blank=True,)
    WX_nickname = models.CharField('微信昵称', max_length=32, null=True, blank=True, default='')
    gender = models.CharField('性别', choices=gender_choices, max_length=32, null=True, blank=True,)
    age = models.CharField('年龄', max_length=32, null=True, blank=True,)
    phone_number = models.CharField('手机号', max_length=32, null=True, blank=True,)
    city = models.CharField('所在城市', max_length=32, null=True, blank=True,)
    create_time = models.DateTimeField('创建日期', max_length=32, null=True, blank=True,)
    vip_grade = models.CharField('用户会员登记', choices=vip_grade_choices, max_length=32, null=True, blank=True, default='')
    is_test = models.CharField('是否测试用户', choices=is_test_choices, max_length=32, null=True, blank=True, default='0')

    def __str__(self):
        return "{} : {}".format(self.WX_nickname, self.phone_number)