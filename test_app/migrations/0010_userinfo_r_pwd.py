# Generated by Django 2.1.7 on 2019-12-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0009_userinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='r_pwd',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]