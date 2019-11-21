from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.django, name='django'),
    re_path(r'^django/', views.django, name='django'),
    re_path(r'^affichage/', views.affichage, name='affichange'),
    re_path(r'^templates/', views.templates, name='templates'),
]