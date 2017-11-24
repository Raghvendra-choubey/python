# Create your models here.
from django.db import models


class Users(models.Model):
    id = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=30)
    alias_nm = models.CharField(max_length=18)
    category = models.CharField(max_length=18)
    g_user_cd = models.CharField(max_length=4)
    password = models.CharField(max_length=18)
    trans_flag = models.CharField(max_length=1)
    user_cd = models.CharField(max_length=1)
    company_id = models.CharField(max_length=4)
    update_dt = models.DateTimeField()
    update_flag = models.CharField(max_length=1)

    class Meta:
        db_table = 'sysmmsuser'
