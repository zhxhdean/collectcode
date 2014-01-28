# coding=utf8
import re, random, time, os, datetime as dt
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from collectcode.models import messages
import user

#@csrf_exempt
@user.logined
def upload_image(request):
    if request.method == 'GET':
        return HttpResponse(messages.INVALID_REQUEST)
    if 'userfile' in request.FILES:
        # ie 普通方式上传
        file_data = request.FILES['userfile']
        file_name = file_data.name
        return save_image(request,file_data, file_name, False)

# 保存文件
def save_image(request,file_data, file_name, html5):
    suffix = file_name[file_name.rindex('.') : len(file_name)]
    if not check_suffix(suffix):
        return render(request,'ajax_upload_result.html',{'result':messages.INVALID_SUFFIX,'resultCode':'failed'})
    if file_data.size/1024/1024.0 > settings.UPLOAD_MAX_SIZE:
        return render(request,'ajax_upload_result.html',{'result':messages.UPLOAD_MAX_SIZE,'resultCode':'failed'})
    new_file_name = '/' + str(int(time.time())) + str(random.randint(0, 1000)) + suffix
    try:
        today = dt.datetime.today()
        dir_path = '/%s/%d/%d/%d' % (settings.MEDIA_PICTURES_DIR, today.year, today.month, today.day)
        create_dir(dir_path)
        with open(settings.MEDIA_ROOT + dir_path + new_file_name , 'wb') as f:
            if html5:
                f.write(file_data)
            else:
                for d in file_data.chunks():
                    f.write(d)
        return render(request,'ajax_upload_result.html',{'result':'file_uploaded','resultCode':'ok','file_name':''.join(['/upload',dir_path , new_file_name])})
    except IOError, e:
        return render(request,'ajax_upload_result.html',{'result':e.strerror,'resultCode':'failed'})
# 创建目录
def create_dir(dir_path):
    if not os.path.exists(settings.MEDIA_ROOT + dir_path):
        os.makedirs(settings.MEDIA_ROOT + dir_path)

# 验证上传文件后缀名
def check_suffix(suffix):
    if suffix.lower() in settings.ALLOW_SUFFIX:
        return True
    return False
