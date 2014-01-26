from django.db import models
from django import forms
import messages
class Link(models.Model):
    class Meta:
        db_table='link'
    id = models.AutoField()
    url = models.CharField(max_length=30)
    text = models.CharField(max_length=10)
    
class LinkForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={'class':'linktext'}),
                         max_length=30,
                         error_messages={'required':messages.NOVALUE_URL,
                                         'invalid':messages.INVALID_URL,
                                         'max_length':messages.MAX_LENGTH_30})
    text = forms.CharField(max_length=10,error_messages={'required':messages.NOVALUE_TEXT
                                                         ,'max_length':messages.MAX_LENGTH_10})