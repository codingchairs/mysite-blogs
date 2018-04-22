from django.contrib import admin
from .models import Post
from simple_history.admin import SimpleHistoryAdmin

#admin.site.register(SimpleHistoryAdmin)
admin.site.register(Post, SimpleHistoryAdmin)