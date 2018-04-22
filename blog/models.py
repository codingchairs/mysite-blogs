# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # class Meta:
    # 	abstract = True


# class my_model(Post):
# 	def has_history(self):
# 		return self.Post.count() > 0 


# class my_model_history(Post):
# 	reason = models.TextField()
# 	history_entry_for = models.ForeignKey(my_model)







