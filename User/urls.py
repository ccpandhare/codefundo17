from django.conf.urls import url
from . import views
from models import Developer

app_name = 'User'


urlpatterns = [
	#/games/
	url(r'^$', views.IndexView.as_view(), name = 'index'),

	url(r'developer/add/$', views.DeveloperCreate.as_view(), name = 'developer-add'),

	#/games/developer/2/
	url(r'developer/(?P<pk>[0-9]+)/$', views.DeveloperUpdate.as_view(), name = 'developer-update'),

	#games/developer/2/delete
	url(r'developer/(?P<pk>[0-9]+)/delete/$', views.DeveloperDelete.as_view(), name = 'developer-delete'),
	
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
	]

#CreateView.as_view(model=Developer, success_url=reverse('index'))
