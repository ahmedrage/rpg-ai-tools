from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexVIew.as_view(), name='index'),
]