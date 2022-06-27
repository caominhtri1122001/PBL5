from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('home/',views.home_view, name="home"),
    path('contact/', views.contact_view, name="contact"),
    path('live/', views.live_view, name="live"),
    path('sensor/', views.sensor_view, name="sensor"),
    path('manage/',views.manage_view, name="manage"),
    path('<str:name>/delete', views.delete_view, name="delete"),
    path('register/', views.register_view, name="register"),
]
