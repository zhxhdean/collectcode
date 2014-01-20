#-*-coding:utf8-*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'collectcode.views.index.home', name='home'),
    url(r'^demo$', 'collectcode.views.blogs.demo'),
    url(r'^admin/login/$', 'collectcode.views.user.login'),
    url(r'^admin/blog/$', 'collectcode.views.blogs.add'),
    url(r'^admin/blog/(?P<id>\d+)/$','collectcode.views.blogs.edit'),
    url(r'^comments/add/$', 'collectcode.views.blogs.add_comments'),
    url(r'^blogs/$', 'collectcode.views.blogs.all'),
    url(r'^blog/(?P<id>\d+)/$', 'collectcode.views.blogs.detail'),
    url(r'^tags/(?P<tag>.*)/$','collectcode.views.tags.search'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',  
        {'document_root': settings.STATIC_ROOT}),
    # url(r'^collectcode/', include('collectcode.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
