from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Actor,Movie,Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer, ActorDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request,actor_id):
    actor = Actor.objects.get(id=actor_id)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','DELETE','PUT'])
def review_detail(request,review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def create_review(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)