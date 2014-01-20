#-*-coding:utf8-*-
from django.db import models

class Tags(models.Model):
    class Meta:
        db_table = 'tags'
    id = models.AutoField(primary_key = True)
    tag = models.CharField()
    last_time = models.DateTimeField(auto_now=True)
    blog_num = models.IntegerField()
    url = models.CharField()
