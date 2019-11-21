from django.conf.urls import url

from .views import init, populate, display

urlpatterns = [
    url('init', init),
    url('populate', populate),
    url('display', display),
]