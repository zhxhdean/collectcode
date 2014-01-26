#-*-coding:utf8-*-
from django.db import models
from django import forms
import messages
class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    passwd = models.CharField()
    
class UserForm(forms.Form):
    username = forms.CharField(max_length=20,error_messages={'max_length':messages.MAX_LENGTH_20,'required':messages.NOVALUE_USER})
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required':messages.NOVALUE_PASSWORD})