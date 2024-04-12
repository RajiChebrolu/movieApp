from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import MovieList, MovieDetail, MovieCategory
=======
from .views import MovieList, MovieDetail  
# from .views import MovieList, MovieDetail, MovieCategory


app_name = 'movies'
>>>>>>> 68e5e43 (UPDATE files)

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]
<<<<<<< HEAD
=======
from .views import MovieList, MovieDetail  
# from .views import MovieList, MovieDetail, MovieCategory


app_name = 'movies'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]
=======
>>>>>>> 68e5e43 (UPDATE files)

# At the moment is not implemented categories

# app_name='movie'
# urlpatterns = [
#     path('', MovieList.as_view(), name='movie_list'),
#     path('category/<str:category>', MovieCategory.as_view(), name='movie_category'), 
#     path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
# ]




<<<<<<< HEAD
>>>>>>> fb08546 (Changes in the following pages,)
=======
>>>>>>> 68e5e43 (UPDATE files)
