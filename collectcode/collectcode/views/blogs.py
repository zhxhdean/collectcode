#-*-coding:utf8-*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.forms.util import ErrorList
from django.utils import simplejson
from django.conf import settings
from collectcode.models import blogs,comments,blogs_tags ,message,tags as tagsModel
from collectcode.views import tags,pager

PAGE_SIZE = 10

#list
def list_page(request,page = 1):
    page = int(page)
    bloglist = blogs.Blogs.objects.all().order_by('-top')[PAGE_SIZE * (page-1):PAGE_SIZE*page]
    total = blogs.Blogs.objects.all().count()
    p = pager.Pager(total,page,PAGE_SIZE)
    pages = p.show()
    blogs_ids = ','.join([str(i.id) for i in bloglist])
    #id不是从用户输入获取,拼接sql安全性还行
    taglist = tagsModel.Tags.objects.raw("select a.id, a.tag,b.blogs_id from tags a \
                                            join blogs_tags b \
                                            on a.id = b.tags_id \
                                            where b.blogs_id in (%s);" %blogs_ids)
    return render(request, 'blogs.html', {'bloglist':bloglist,'taglist':taglist,'pages':pages})



def detail(request,id):
    id =int(id)
    try:
        blog = blogs.Blogs.objects.get(id=id)
        blog.views = blog.views + 1
        blog.save()
        ls = comments.Comments.objects.filter(blog_id=id)
        form = comments.CommentsForm()
        return render(request,'blog.html',{'blog':blog,'list':ls,'form':form})
    except blogs.Blogs.DoesNotExist:
        return redirect('/')
    except:
        raise


def demo(request):
    return render(request,'demo.html')


#add new blog
def add(request):
    if settings.SESSION_KEY not in request.session:
        return redirect('/admin/login')
    if request.method == 'POST':
        form = blogs.BlogsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            top = form.cleaned_data['top']
            note = form.cleaned_data['note']
            b = blogs.Blogs(title=title,top=top,note=note)
            #save blog
            b.save()
            tag = form.cleaned_data['tag']
            #save tag
            for t in tag.split(','):
                #tag
                tag_d = tags.save(t, 1)                
                tags.save_blogs_tags(b.id,tag_d.id)
            form = blogs.BlogsForm()
            return render(request,'add_blog.html',{'msg':message.SUCCESS,'form':form})
        else:
            return render(request,'add_blog.html',{'form':form})
    else:
        form = blogs.BlogsForm()
        return render(request,'add_blog.html',{'form':form})

#edit blog
def edit(request,id):
    if settings.SESSION_KEY not in request.session:
        return redirect('/admin/login')
    if request.method == 'POST':        
        form = blogs.BlogsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            top = form.cleaned_data['top']
            note = form.cleaned_data['note']
            b = blogs.Blogs(id=int(id),title=title,top=top,note=note)
            b.save()
            tag = form.cleaned_data['tag']
            old_tag = request.POST['hd_tag']
            #insert new tag
            i_tag = set(tag.split(',')) - set(old_tag.split(','))
            #save new tag
            for t in i_tag:
                #tag
                tag_d = tags.save(t, 1)
                tags.save_blogs_tags(id,tag_d.id)
            #update old tag or delete old tag
            u_tag = set(old_tag.split(',')) - set(tag.split(','))
            for t in u_tag:                
                tags.update(t)
                tags.delete_blogs_tags(id, t)            
            return render(request,'edit_blog.html',{'msg':message.SUCCESS,'form':form})
        else:
            return render(request,'edit_blog.html',{'form':form})
    else:
        try:
            d = blogs.Blogs.objects.get(id=id)
            tags_ls = tagsModel.Tags.objects.raw('select t.id,t.tag from tags t join blogs_tags b on t.id = b.tags_id where b.blogs_id = %s;',[id])
            form = blogs.BlogsForm(initial={'title':d.title,'note':d.note,'top':d.top,'tag':','.join([str(_t.tag) for _t in tags_ls])})
            return render(request,'edit_blog.html',{'form':form})
        except blogs.Blogs.DoesNotExist:
            return redirect('/')

#delete blog
def delete(request,id):
    if settings.SESSION_KEY not in request.session:
        return redirect('/admin/login')
    try:
        d = blogs.Blogs.objects.get(id = id)
        d.delete()
        tag_ls = blogs_tags.Blogs_tags.objects.filter(blogs_id = id)
        for t in tag_ls:
            tags.update_id(t.tags_id)
            tags.delete_blogs_tags_id(t.id)
        return redirect(request.META['HTTP_REFERER'])
    except blogs.Blogs.DoesNotExist:
            return redirect('/')
    
def add_comments(request):
    json ={}
    if request.method == 'POST':        
        form = comments.CommentsForm(request.POST)
        try:
            if form.is_valid():  
                blog_id = int(request.POST['blogid'])          
                email = form.cleaned_data['email']
                comment = form.cleaned_data['comment']               
                try:
                    c = comments.Comments(email=email,comment=comment,blog_id=blog_id)
                    c.save()
                    json['msg'] = message.SUCCESS
                    json['error'] =u'0'
                except:
                    json['msg'] = message.PROGRAM_EXCEPTION
                    json['error'] =u'1'
            else:
                err ={}
                if 'email' in form.errors:
                    err['e']= unicode(form.errors['email'].as_text())
                if 'comment' in form.errors:
                    err['c'] = unicode(form.errors['comment'].as_text())
                json['error'] =u'1'
                json['msg'] = err
        except Exception:
            json['msg'] = message.PROGRAM_EXCEPTION 
            json['error'] =u'1'
    else:
        json['msg'] = message.INVALID_REQUEST
        json['error'] =u'1'
    return HttpResponse(simplejson.dumps(json, ensure_ascii=False),content_type='application/json')
    