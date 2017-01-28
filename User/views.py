from django.shortcuts import render

class IndexView(generic.ListView):
	template_name = 'User/index.html'

	def get_queryset(self):
		return User.models.all()

class DetailView(generic.DetailView):
	model = User
	template_name = 'User/detail.html'

