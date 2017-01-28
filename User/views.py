from django.shortcuts import render

class IndexView(generic.ListView):
	template_name = 'User/index.html'

	def get_queryset(self):
		return User.models.all()

