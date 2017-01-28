from __future__ import unicode_literals

from django.db import models

class User(models.Model):

	user_name = models.CharField(max_length=100)
	user_profile_picture = models.CharField(max_length=1000)
	user_age = models.IntegerField(default=20)
	user_profession = models.CharField(max_length=50)
	user_tags = models.CharField(max_length = 1000)

	def __unicode__(self):
		return self.user_name