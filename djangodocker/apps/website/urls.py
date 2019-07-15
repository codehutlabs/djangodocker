from django.urls import path

from djangodocker.apps.website import views


urlpatterns = [
    path("", views.home, name="home"),
]
