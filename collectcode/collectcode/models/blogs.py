#-*-coding:utf8-*-
from django.db import models
from django import forms
import message
class Blogs(models.Model):
    class Meta:
        db_table = 'blogs'
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    note = models.CharField()
    url = models.CharField(default='')
    tags = models.CharField()
    last_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    top = models.BooleanField(default=0)
    
class BlogsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'blogtext'}),max_length=100,error_messages={'required':message.NOVALUE_TITLE})
    note = forms.CharField(widget=forms.Textarea,error_messages={'required':message.NOVALUE_NOTE})
    top = forms.BooleanField(widget=forms.CheckboxInput,required=False)
    tag = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'blogtext'}))