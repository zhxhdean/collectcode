#-*-coding:utf8-*-
from django.shortcuts import render, redirect
from django.db.models import Max,Min
from django.conf import settings
from collectcode.models import blogs,tags,user,comments

def home(request):
    bloglist = blogs.Blogs.objects.all().order_by('-top')[0:5]
    taglist = tags.Tags.objects.raw("select a.id, a.tag,b.blogs_id from tags a join blogs_tags b on a.id = b.tags_id;")
    return render(request, 'index.html', {'bloglist':bloglist,'taglist':taglist})

def base(request):
    #right tags
    tagslist = tags.Tags.objects.all()
    max_num = int(tagslist.aggregate(Max('blog_num'))['blog_num__max'])
    min_num = int(tagslist.aggregate(Min('blog_num'))['blog_num__min'])
    ls = []
    for t in tagslist:
        ls.append('<a href="/tags/%s" title="topic %s" style="font-size:%spt">%s</a>' % (t.tag,t.blog_num,(8+14.0*t.blog_num/(max_num-min_num)),t.tag))
    
    #用户
    user_info = None
    if settings.SESSION_KEY in request.session:
        uid = request.session[settings.SESSION_KEY]
        user_info = user.User.objects.get(id=uid)

    #comments 
    clist = comments.Comments.objects.all().order_by('-last_time')[0:5]    
    return {'tagsls' : ''.join(ls),'user':user_info,'clist':clist}


def calendar(request):
    return render(request,'calendar.html')