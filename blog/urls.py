from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]
