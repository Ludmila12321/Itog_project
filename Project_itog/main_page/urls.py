from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    ]