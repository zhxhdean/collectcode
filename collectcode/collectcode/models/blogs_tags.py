#-*-coding:utf8-*-
from django.db import models
from collectcode.models import blogs,tags
class Blogs_tags(models.Model):
    class Meta:
        db_table = 'blogs_tags'
    id = models.AutoField(primary_key = True)
    blogs_id = models.IntegerField()
    tags_id = models.IntegerField()
    