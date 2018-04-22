from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^chairs/profiles/new/$', views.NewUserProfileView.as_view(), name = "new-user-profile"),
    url(r'^chairs/($P<pk>\d+)/edit/$', views.EditUserProfileView.as_view(), name = "edit-user-profile"),   
]
