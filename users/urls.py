from django.urls import path
from . import views
from allauth.urls import urlpatterns


urlpatterns = [
    path("", views.home, name="home"),
]
