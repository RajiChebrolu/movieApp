from django.urls import path

from .views import MovieList, MovieDetail, MovieCategory

from .views import MovieList, MovieDetail  
# from .views import MovieList, MovieDetail, MovieCategory


app_name = 'movies'


urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]


from .views import MovieList, MovieDetail  
# from .views import MovieList, MovieDetail, MovieCategory


app_name = 'movies'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]


# At the moment is not implemented categories

# app_name='movie'
# urlpatterns = [
#     path('', MovieList.as_view(), name='movie_list'),
#     path('category/<str:category>', MovieCategory.as_view(), name='movie_category'), 
#     path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
# ]




