from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms_test.views.home', name='home'),
    # url(r'^cms_test/', include('cms_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),a
    (r'^page_info', 'cms_test.get_data.page_info'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

#if settings.DEBUG:
#    urlpatterns = patterns('',
#    url(r'media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root':settings.MEDIA_ROOT, 'show_indexs': True}),
#    url(r'', include('django.contrib.staticfiles.urls')),
#) + urlpatterns    
