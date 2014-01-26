#-*-coding:utf8-*-
import sys
from hashlib import md5
from django.shortcuts import render,redirect
from django.forms.util import ErrorList
from django.conf import settings
from collectcode.models import user,messages

def login(request):
    if request.method == 'GET':
        form = user.UserForm()        
        next = '/'
        if request.GET.get('from'):
            next = request.GET.get('from')
        return render(request,'login.html',{'form':form,'next':next})
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
                    return redirect(request.POST['next'])
                else:
                    form.errors['password'] = ErrorList([messages.INVALID_PASSWORD])
                    return render(request,'login.html',{'form':form})
            except user.User.DoesNotExist:
                form.errors['username'] = ErrorList([messages.INVALID_USER])
                return render(request,'login.html',{'form':form})
            except:
                print sys.exc_info()[0]
                form.errors['username'] = ErrorList([messages.PROGRAM_EXCEPTION])
                return render(request,'login.html',{'form':form})           
        else:
            return render(request,'login.html',{'form':form})


def logout(request):
    try:
        del request.session[settings.SESSION_KEY]
    except KeyError:
        pass
    return redirect('/')

def logined(v):
    def new_view(request,*args,**kwargs):
        if settings.SESSION_KEY not in request.session:
            referer = request.META['PATH_INFO']
            return redirect('/admin/login/?from=%s'%referer)
        return v(request,*args,**kwargs)
    return new_view