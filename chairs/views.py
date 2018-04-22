# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import FormView, UpdateView

from . forms import UserProfileForm
from . models import UserProfile 


class NewUserProfileView(FormView):
    template_name = "user_profile.html"
    form_class = UserProfileForm
    print "here i am2333"

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("http://127.0.0.1:8000/")

class EditUserProfileView(UpdateView):
	model = UserProfile 
	form_class = UserProfileForm
	template_name = "chairs/user_profile.html"

	def get_objects(self, *args, **kwargs):
		user = get_objects_or_404(User, pk=self.kwargs['pk'])

		return user.userprofile

	def get_success_url(self, *args, **kwargs):
		return reverse("some url name")