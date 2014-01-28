from django.shortcuts import render

def home(request):
    return render(request,'tinymce.html')

def ajax_upload(request):
    return render(request,'blank.html')