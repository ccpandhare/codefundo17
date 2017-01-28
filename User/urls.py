from django.conf.urls import url
from . import views
from models import Developer

app_name = 'User'


urlpatterns = [
	#/games/
	url(r'^$', views.IndexView.as_view(), name = 'index'),

	url(r'developer/add/$', views.DeveloperCreate.as_view(), name = 'developer-add'),

	#/games/developers
	url(r'^developers/$', views.DeveloperDetailsView.as_view(), name = 'developer-detail'),
	#/games/developer/2/
	url(r'developer/(?P<pk>[0-9]+)/$', views.DeveloperUpdate.as_view(), name = 'developer-update'),

	#games/developer/2/delete
	url(r'developer/(?P<pk>[0-9]+)/delete/$', views.DeveloperDelete.as_view(), name = 'developer-delete'),
	
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

	url(r'^devlogin(?P<pk>[0-9]+)/$', views.LoginDetailView.as_view(), name = 'login-detail'),
	

	url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
	]

#CreateView.as_view(model=Developer, success_url=reverse('index'))
