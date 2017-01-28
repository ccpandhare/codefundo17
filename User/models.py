from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class User(models.Model):

	user_name = models.CharField(max_length=100)
	user_profile_picture = models.FileField(max_length=1000)
	user_age = models.IntegerField(default=20)
	user_profession = models.CharField(max_length=50)
	user_tags = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.user_name

class Developer(models.Model):

	developer_name = models.CharField(max_length=100)
	developer_logo = models.FileField(max_length=1000)
	developer_headquarters = models.CharField(max_length=1000)
	developer_tags = models.CharField(max_length=100)

	def __unicode__(self):
		return self.developer_name

	def get_absolute_url(self):
		return reverse('User:login-detail', kwargs={'pk':self.pk})

	def developer_tag_list(self):
		return self.developer_tags.split(',')