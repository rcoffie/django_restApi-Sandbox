from watchlist_app.models import Movie 
from watchlist_app.api.serailizers import MovieSerailizer
from rest_framework.response import Response 
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
  movies = Movie.objects.all()
  serializer = MovieSerailizer(movies,many=True)
  return Response (serializer.data)
  
  
@api_view()
def movie_detail(request, pk):
  movie = Movie.objects.get(id=pk)
  serializer = MovieSerailizer(movie)
  return Response (serializer.data)