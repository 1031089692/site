from django.contrib import admin
from test_app.models import *

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(AccessFrequencyVerification)
admin.site.register(Order)
admin.site.register(OrderReplyRecord)
admin.site.register(Customer)
admin.site.register(FoodDetails)