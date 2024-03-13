from django.urls import path
from . import views

urlpatterns = [
    path('animal_catalog/', views.animal_catalog, name='animal_catalog'),
]