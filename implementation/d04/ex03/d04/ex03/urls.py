from django.urls import re_path
from ex03 import views

urlpatterns = [
    re_path(r'^$', views.ex03),
]