from django.conf.urls import url, include
from django.contrib import admin

from mysite.views import hello
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #all-auth
    url(r'^accounts/', include('allauth.urls')),

    url(r'^hello/$', hello),
    url('^$', views.Home.as_view(), name = 'home'),

    url(r'^chairs/', include('chairs.urls')),
    url(r'^blog/', include('blog.urls')),
    
]
