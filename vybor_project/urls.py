from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^about/strategy/', include('strategy.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^documents/', include('documents.urls')),
    #url(r'^advisors/', include('advisors.urls')),
    #url(r'^direction/', include('direction.urls')),
    #url(r'^partners/', include('partners.urls')),
    url(r'^media/video/', include('video.urls')),
    url(r'^media/images/', include('images.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
