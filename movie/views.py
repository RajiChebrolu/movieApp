from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks

# Create your views here.
class MovieList(ListView):
    model = Movie
<<<<<<< HEAD
<<<<<<< HEAD
=======
    template_name='movie/movie_list.html'
>>>>>>> fb08546 (Changes in the following pages,)
=======
    template_name='movie/movie_list.html'
>>>>>>> 68e5e43 (UPDATE files)
    paginate_by =1


class MovieDetail(DetailView):
    model = Movie
<<<<<<< HEAD
<<<<<<< HEAD
=======
    template_name='movie/movie_detail.html'
>>>>>>> fb08546 (Changes in the following pages,)
=======
    template_name='movie/movie_detail.html'
>>>>>>> 68e5e43 (UPDATE files)

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count +=1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by =3
    # changed 1 to 3 and added this line
    template_name = 'movie/movie_category_list.html'

    def get_queryset(self):
        category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

  
    def get_context_data(self, **kwargs): 
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
<<<<<<< HEAD
<<<<<<< HEAD
        
=======
=======
>>>>>>> 68e5e43 (UPDATE files)
        
        
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks








#   OPTION 2
# Createn an other option, but this one did't work very well, keept the first
# and added the paths to the templates 


# from django.shortcuts import render

# # from .views import MovieList, MovieDetail
# from django.views.generic import ListView, DetailView
# from .models import Movie
# from django.contrib.auth.mixins import LoginRequiredMixin


# class MovieListView( ListView):
#     model = Movie
#     template_name = 'movie/movie_list.html'  # template
#     # login_url = '/accounts/login/' 
    

# class MovieDetailView(DetailView):
#     model = Movie
#     template_name = 'movie/movie_detail.html'  #  template


# class MovieLinksListView(ListView):
#     model = MovieLinks
#     template_name = 'movie/movie_links_list.html' 

# class MovieLinksDetailView(DetailView):
#     model = MovieLinks
#     template_name = 'movie/movie_links_detail.html'  



<<<<<<< HEAD
>>>>>>> fb08546 (Changes in the following pages,)
=======
>>>>>>> 68e5e43 (UPDATE files)
