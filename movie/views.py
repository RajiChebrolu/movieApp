from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks

# Create your views here.
class MovieList(ListView):
    model = Movie
    template_name='movie/movie_list.html'
    paginate_by =2


class MovieDetail(DetailView):
    model = Movie
    template_name='movie/movie_detail.html'

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
        
        
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks







from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, MovieLinks
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.dates import YearArchiveView

# # links for contact page:
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from .forms import ContactForm

class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'
        
    def get_context_data(self, **kwargs): 
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        print(context)
        return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('movies:detail') 

class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 3

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
   

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj

   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        context['links'] = MovieLinks.objects.filter(movie=movie)
        return context

class MovieCategory(ListView):
    model = Movie
    paginate_by =2

    def get_queryset(self):
        self.category = self.kwargs['category']
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
    
class MovieLanguage(ListView):
    model = Movie
    paginate_by =2

    def get_queryset(self):
        self.language = self.kwargs['language']
        return Movie.objects.filter(language=self.language)

  
    def get_context_data(self, **kwargs): 
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context
    
class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'production_of_year'
    make_object_list = True
    allow_future = True
    print(queryset)


