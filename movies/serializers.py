from rest_framework import serializers
from .models import Movie, Actor, Review

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = '__all__'

    def get_movie(self, obj):
        return obj.movie.title

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorDetailSerializer(serializers.ModelSerializer):
    movie_movies = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = '__all__'

    def get_movie_movies(self, obj):
        return [movie.title for movie in obj.movie_movies.all()]
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    movie_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_actors(self, obj):
        return [actor.name for actor in obj.actors.all()]

    def get_movie_reviews(self, obj):
        return [review.content for review in obj.movie_reviews.all()]