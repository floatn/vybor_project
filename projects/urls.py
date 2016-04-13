from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.ProjectsPageView.as_view(), name = 'projects-index'),
]
