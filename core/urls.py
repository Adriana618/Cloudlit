from django.urls import path

from core import views

urlpatterns = [path("python", views.execute)]
