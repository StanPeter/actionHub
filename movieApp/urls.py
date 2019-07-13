from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    
    path('create/', views.movie_create, name='movie_create'),

    path('detail/<str:id>/edit', views.movie_edit, name="movie_edit"),

    path('detail/<str:id>/delete/', views.movie_delete, name='movie_delete'),
]

