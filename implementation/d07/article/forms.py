from django.forms import forms
from django.forms import ModelForm
from .models import ArticleModel, UserFavoriteArticle


class AddFavoriteArticleForm(ModelForm):
    class Meta:
        model = UserFavoriteArticle
        fields = []


class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'synopsis', 'content', ]
