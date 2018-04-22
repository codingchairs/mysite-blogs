# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User 

class UserProfile(models.Model):
	# let us add some simple fields to profile.
	user = models.OneToOneField(User)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=10)

	def __unicode__(self):
		return u"%s" % self.user 
		