from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_movies, name='list_movies'),  # ✅ important!
    path('add/', views.add, name='add_movie'),
]
