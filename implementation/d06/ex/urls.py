from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
	path('signup/', views.signup),
	path('logout/', views.logout),
]