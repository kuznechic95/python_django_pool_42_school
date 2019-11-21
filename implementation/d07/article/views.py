from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView, DetailView, RedirectView, CreateView
from .models import ArticleModel, UserFavoriteArticle
from django.contrib.auth.forms import AuthenticationForm
from .forms import AddFavoriteArticleForm, ArticleForm


class HomeView(ListView):
    model = ArticleModel
    template_name = "article/articles.html"


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "article/login.html"
    success_url = "/"


class ArticleView(ListView):
    model = ArticleModel
    paginate_by = 50
    template_name = "article/articles.html"


class PublicationsView(ListView):
    model = ArticleModel
    template_name = "article/publications.html"


class ArticleDetailView(DetailView, FormView):
    model = ArticleModel
    template_name = "article/detail.html"
    form_class = AddFavoriteArticleForm
    success_url = "/favorites"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            item = form.save(commit=False)
            item.user = self.object.author
            item.article = self.object
            item.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FavoritesView(ListView):
    model = UserFavoriteArticle
    template_name = "article/favorites.html"


class PublishView(FormView):
    form_class = ArticleForm
    template_name = "article/publish.html"
    success_url = "/"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        item.save()
        return super().form_valid(form)
