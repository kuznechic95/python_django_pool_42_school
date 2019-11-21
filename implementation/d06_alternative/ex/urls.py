from django.conf.urls import url

from .views import index, signup, signin, signout, createtip, vote, delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', index),
    url('login', signin),
    url('logout', signout),
    url('signup', signup),
    url('createtip', createtip),
    url('vote', vote),
    url('delete', delete),
]