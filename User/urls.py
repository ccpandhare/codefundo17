from django.conf.urls import url
from . import views

app_name = 'User'


urlpatterns = [
	#/games/
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	]

