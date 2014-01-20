#-*-coding:utf8-*-
import sys
from hashlib import md5
from django.shortcuts import render,redirect
from django.forms.util import ErrorList
from django.conf import settings
from collectcode.models import user,message

def login(request):
    if request.method == 'GET':
        form = user.UserForm()
        return render(request,'login.html',{'form':form})
    elif request.method =='POST':
        form = user.UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user_info = user.User.objects.get(name=username)
                if md5(password).hexdigest() == user_info.passwd:
                    request.session[settings.SESSION_KEY] = user_info.id
                    request.session.set_expiry(0)
                    return redirect('/')
                else:
                    form.errors['password'] = ErrorList([message.INVALID_PASSWORD])
                    return render(request,'login.html',{'form':form})
            except user.User.DoesNotExist:
                form.errors['username'] = ErrorList([message.INVALID_USER])
                return render(request,'login.html',{'form':form})
            except:
                print sys.exc_info()[0]
                form.errors['username'] = ErrorList([message.PROGRAM_EXCEPTION])
                return render(request,'login.html',{'form':form})           
        else:
            return render(request,'login.html',{'form':form})
        
    