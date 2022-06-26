from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name="home"),
    path('manage/',views.manage_view, name="manage"),
    path('<str:name>/delete', views.delete_view, name="delete"),
]
