from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.NewsPageView.as_view(), name = 'index'),
]
