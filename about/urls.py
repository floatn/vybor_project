from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^advisors', views.AdvisorListView.as_view(), name = 'about_advisors'),
	url(r'^direction', views.DirectionListView.as_view(), name = 'about_direction'),
	url(r'^partners', views.PartnerListView.as_view(), name = 'about_partners'),
]
