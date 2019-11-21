from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('publications/', login_required(views.PublicationsView.as_view()), name='publications'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('favorites/', login_required(views.FavoritesView.as_view()), name='favorites'),
    path('detail/<int:pk>/add_favorite/', login_required(views.ArticleDetailView.as_view()), name='add_favorite'),
    path('publish/', login_required(views.PublishView.as_view()), name='publish'),
]
