from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.ProjectsPageView.as_view(), name = 'projects'),
	url(r'^details/(?P<pk>[0-9]+)/$', views.ProjectDetailsPageView.as_view(), name='project-details'),
]
