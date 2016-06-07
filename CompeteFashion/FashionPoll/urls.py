from django.conf.urls import patterns, url
from FashionPoll import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^participate/$', views.participate, name='participate'),
]
