from django.urls import path
from . import views


urlpatterns = [
    # index route for movies
    path('', views.index, name='index'),
    # new/create route for movies
    path('create/', views.create, name='create'),
    # edit/update route for movies
    path('detail/<str:id>/edit', views.edit, name="edit"),
    # destroy route for movies
    path('detail/<str:id>/delete/', views.delete, name='delete'),
]
