from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

class IndexView(generic.ListView):
	template_name = 'User/index.html'

	def get_queryset(self):
		return User.models.all()

class DetailView(generic.DetailView):
	model = User
	template_name = 'User/detail.html'

