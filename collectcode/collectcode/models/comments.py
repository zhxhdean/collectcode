#-*-coding:utf8-*-
from django.db import models
from django import forms
import blogs,messages
class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    comment = models.CharField()
    last_time = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(blogs.Blogs)
    
class CommentsForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'emailtext'}),error_messages={'required':messages.NOVALUE_EMAIL,'invalid':messages.INVALID_EMAIL})
    comment = forms.CharField(min_length=5,max_length=250,error_messages={'required':messages.NOVALUE_COMMENT,'min_length':messages.MIN_LENGTH_5
                                                                          ,'max_length':messages.MAX_LENGTH_250},
                              widget=forms.Textarea(attrs={'rows':15,'cols':90}))