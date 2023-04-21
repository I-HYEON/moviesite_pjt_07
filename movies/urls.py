from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('api/v1/actors/', views.actor_list, name='actor_list'),
    path('api/v1/actors/<int:actor_id>/', views.actor_detail, name=',actor_detail'),
    path('api/v1/movies/', views.movie_list, name='movie_list'),
    path('api/v1/movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('api/v1/reviews/', views.review_list, name='review_list'),
    path('api/v1/reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('api/v1/movies/<int:movie_id>/reviews/', views.create_review, name='create_review'),
]