from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField('Actor', related_name='movie_movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='movie_reviews')