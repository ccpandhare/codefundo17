from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import User, Developer
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from forms import UserForm


class IndexView(generic.ListView):
	template_name = 'User/index.html'

	def get_queryset(self):
		return User.objects.all()

'''
class DetailView(generic.DetailView):
	model = User
	template_name = 'User/detail.html'

class UserFormView(View):

	form_class = UserForm
	template_name = 'User/registration-form.html'

	def get(self, request):
		
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#output clean data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
 			user.set_password(password)

 			user.save()

 			user = authenticate(username=username, password=password)

 			if user is not None:
 				if user.is_active:

 					login(request, user)

 					return redirect('User:')

 		return render(request, self.template_name, {'form':form})

 '''
class DeveloperCreate(CreateView):

	model = Developer
	fields = ['developer_name', 'developer_logo', 'developer_headquarters', 'developer_tags'] 

class DeveloperUpdate(UpdateView):

	model = Developer
	fields = ['developer_name', 'developer_logo', 'developer_headquarters', 'developer_tags'] 

class DeveloperDelete(DeleteView):

	model = Developer

	success_url = reverse_lazy('User:index')