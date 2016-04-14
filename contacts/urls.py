from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.ContactListView.as_view(), name = 'contacts'),
]
