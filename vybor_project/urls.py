from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^$', include('contacts.urls')),
    url(r'^$', include('projects.urls')),
]
