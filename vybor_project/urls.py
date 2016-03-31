from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^documents/', include('documents.urls', namespace='documents')),
    url(r'^advisors/', include('advisors.urls', namespace='advisors')),
    url(r'^strategy/', include('strategy.urls', namespace='strategy')),
    url(r'^partners/', include('partners.urls', namespace='partners')),
    url(r'^video/', include('video.urls', namespace='video')),
    url(r'^images/', include('images.urls', namespace='images')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
