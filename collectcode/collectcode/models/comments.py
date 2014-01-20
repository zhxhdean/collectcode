#-*-coding:utf8-*-
from django.db import models
from django import forms
from collectcode.models import blogs,message
class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    comment = models.CharField()
    last_time = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(blogs.Blogs)
    
class CommentsForm(forms.Form):
    email = forms.EmailField(error_messages={'required':message.NOVALUE_EMAIL,'invalid':message.INVALID_EMAIL})
    comment = forms.CharField(min_length=5,max_length=250,error_messages={'required':message.NOVALUE_COMMENT,'min_length':message.MIN_LENGTH_5
                                                                          ,'max_length':message.MAX_LENGTH_250},
                              widget=forms.Textarea(attrs={'rows':5,'cols':90}))