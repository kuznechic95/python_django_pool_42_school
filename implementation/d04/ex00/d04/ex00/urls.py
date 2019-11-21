from django.conf.urls import re_path
from .views import IndexPageView

urlpatterns = [
    re_path(r'^$', IndexPageView.as_view(), name='ex00'),

]
