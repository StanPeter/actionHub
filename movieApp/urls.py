from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    
    path('create/', views.movie_create, name='movie_create'),
]

