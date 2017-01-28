from django.conf.urls import url
from . import views

app_name = 'User'


urlpatterns = [
	#/games/
	url(r'^$', views.IndexView.as_view(), name = 'index'),

	url(r'developer/add/$', views.DeveloperCreate.as_view(), name = 'user-add'),

	#/games/developer/2/
	url(r'developer/(?P<pk>[0-9]+)/$', views.DeveloperUpdate.as_view(), name = 'user-update'),

	#games/developer/2/delete
	url(r'developer/(?P<pk>[0-9]+)/delete/$', views.DeveloperDelete.as_view(), name = 'user-delete'),
	]

