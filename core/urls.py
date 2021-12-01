from django.urls import path

from core import views

urlpatterns = [
    path("", views.login),
    path("python", views.execute),
]
