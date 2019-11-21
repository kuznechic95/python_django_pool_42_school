from django.urls import re_path
from ex02 import views

urlpatterns = [
    re_path(r'^$', views.main, name='ex02'),
    re_path(r'^post_new', views.post_new, name='post_new'),
]