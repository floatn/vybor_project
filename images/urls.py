from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.ImagePageView.as_view(), name = 'images'),
	#url(r'^media/images/page(?P<page>\d+)/$', views.ImagePageView.as_view(), name = 'images'),
]
