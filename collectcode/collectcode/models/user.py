#-*-coding:utf8-*-
from django.db import models
from django import forms
import message
class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    passwd = models.CharField()
    
class UserForm(forms.Form):
    username = forms.CharField(max_length=20,error_messages={'max_length':message.MAX_LENGTH_20,'required':message.NOVALUE_USER})
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required':message.NOVALUE_PASSWORD})