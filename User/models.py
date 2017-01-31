from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django import forms


'''

class User(models.Model):

	user_name = models.CharField(max_length=100)
	user_profile_picture = models.FileField(max_length=1000)
	user_age = models.IntegerField(default=20)
	user_profession = models.CharField(max_length=50)
	user_tags = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.user_name
'''

class Developer(models.Model):

   	user = models.OneToOneField(User, default=None)
   	developer_name = models.CharField(max_length=100, default='')
   	developer_logo = models.FileField()
   	developer_headquarters = models.CharField(max_length=100)
	developer_address = models.CharField(max_length=1000, default = '')
	developer_contact = models.CharField(max_length=100, default = '')
   	developer_tags = models.CharField(max_length=100, default='Separate by comma')

   	def __unicode__(self):
		return self.developer_name

	def get_absolute_url(self):
		return reverse('User:detail', kwargs={'pk':self.pk})

	def developer_tag_list(self):
		return self.developer_tags.split(',')

class UserProfile(models.Model):
        # This field is required.
    user = models.OneToOneField(User)
        # These fields are optional
    developer_name = models.CharField(max_length=100)
    developer_logo = models.FileField()
    developer_headquarters = models.CharField(max_length=100)
    developer_tags = models.CharField(max_length=100)

    def __unicode__(self):
		return self.user.username

from django.forms import ModelForm

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = UserProfile
                fields = ['developer_name', 'developer_logo', 'developer_headquarters', 'developer_tags']
