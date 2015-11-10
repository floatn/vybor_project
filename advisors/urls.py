from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.AdvisorsPageView.as_view(), name = 'index'),
]
