from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.StrategyPageView.as_view(), name = 'strategy'),
]
