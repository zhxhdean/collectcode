#-*-coding:utf8-*-
from django.shortcuts import render
from collectcode.models import blogs,blogs_tags,tags
import pager


PAGE_SIZE = 10
def search(request,tag,page =1):
    page = int(page)
    all_list = blogs.Blogs.objects.raw('select count(1) as id from blogs a \
                                         join blogs_tags b on a.id = b.blogs_id \
                                         join tags c on c.id = b.tags_id \
                                         where c.tag=%s order by a.top desc', [tag])
    total = int(''.join([str(e.id) for e in all_list]))
    p = pager.Pager(total,page,PAGE_SIZE)
    pages = p.show()
    
    bloglist = blogs.Blogs.objects.raw('select a.id,a.title,a.note from blogs a \
                                         join blogs_tags b on a.id = b.blogs_id \
                                         join tags c on c.id = b.tags_id \
                                         where c.tag=%s order by a.top desc', [tag])[PAGE_SIZE * (page-1):PAGE_SIZE*page]
    taglist = tags.Tags.objects.raw("select a.id, a.tag,b.blogs_id from tags a\
     join blogs_tags b on a.id = b.tags_id \
     where b.blogs_id in (%s);" %','.join([str(i.id) for i in bloglist]))
    return render(request,'tags.html',{'bloglist':bloglist,'tag':tag,'pages':pages,'taglist':taglist})

#是否存在tag,返回tag
def exist(tag):
    try:
        return tags.Tags.objects.get(tag = tag)
    except tags.Tags.DoesNotExist:
        return None
    except:
        return None

#是否存在tag,返回tag
def exist_id(id):
    try:
        return tags.Tags.objects.get(id = id)
    except tags.Tags.DoesNotExist:
        return None
    except:
        return None    

#保存tag
def save(tag,num=0):
    t = exist(tag)
    if not t:
        t = tags.Tags(tag = tag,blog_num = num,url = tag)
        t.save()
        return t
    else:
        t.blog_num = t.blog_num + num
        t.save()
        return t
        
#保存 blogs_tags    
def save_blogs_tags(bid,tid):
    b = blogs_tags.Blogs_tags(blogs_id = bid,tags_id = tid)
    b.save()
    
#删除 blogs_tags  
def delete_blogs_tags(bid,tag):
    t = exist(tag)
    if t:
        try:
            b = blogs_tags.Blogs_tags.objects.get(blogs_id = bid,tags_id = t.id)
            b.delete()
        except blogs_tags.Blogs_tags.DoesNotExist:
            pass

#删除 blogs_tags  
def delete_blogs_tags_id(id):
    t = exist_id(id)   
    t.delete()

#更新tag
def update(tag):
    t = exist(tag)
    if t:
        blog_num = t.blog_num - 1
        if blog_num <= 0:
            blog_num = 0
        t.blog_num = blog_num
        t.save()
        
def update_id(id):        
    t = exist_id(id)
    if t:
        blog_num = t.blog_num - 1
        if blog_num <= 0:
            blog_num = 0
        t.blog_num = blog_num
        t.save()