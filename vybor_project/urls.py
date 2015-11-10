from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^documents/', include('documents.urls', namespace='documents')),
    url(r'^advisors/', include('advisors.urls', namespace='advisors')),
]
if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                        'document_root': settings.MEDIA_ROOT,
                                }),
                                   )
