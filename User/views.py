from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Developer, UserProfile
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from forms import UserForm, UserProfileForm
from django.template import RequestContext
from Code_Fun_Do.settings import MEDIA_ROOT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.core.exceptions import *

class IndexView(generic.ListView):
	template_name = 'User/index.html'

	def get_queryset(self):
		return Developer.objects.all()
	
class DeveloperDetailsView(generic.ListView):
	template_name = 'User/developerpage.html'

	def get_queryset(self):
		return Developer.objects.all()


class DetailView(generic.DetailView):
	model = Developer
	template_name = 'User/detail.html'

class LoginDetailView(generic.DetailView):
	model = Developer
	template_name = 'User/detaillogin.html'

	#def get_queryset(self):
	#	my_list = Developer.developer_tags.split(",")  
	#	return my_list

class UserFormView(View):

	form_class = UserForm
	template_name = 'User/registration_form.html'

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

 					return redirect('User:developer-add')

 		return render(request, self.template_name, {'form':form})


class DeveloperCreate(CreateView):

	model = Developer
	fields = ['developer_name', 'developer_logo', 'developer_headquarters', 'developer_tags'] 

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeveloperCreate, self).dispatch(*args, **kwargs)

class DeveloperUpdate(UpdateView):

	model = Developer
	fields = ['developer_name', 'developer_logo', 'developer_headquarters', 'developer_tags'] 

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeveloperUpdate, self).dispatch(*args, **kwargs)



class DeveloperDelete(DeleteView):

	model = Developer

	success_url = reverse_lazy('User:index')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeveloperDelete, self).dispatch(*args, **kwargs)

class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    template_name ='User/login.html'
    success_url = '/user/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/user/')


def search(request):
	
	developers = []

	if request.GET.get('search'):

		search = request.GET.get('search')
		developers = Developer.objects.filter(developer_tags__contains=search)



	return render(request, 'User/search.html', {'developers':developers,})

