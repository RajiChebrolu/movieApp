from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, MovieLinks
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.dates import YearArchiveView

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
    success_url = reverse_lazy('movies:login') 

class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 3
    template_name = 'movie/movie_list.html'
    paginate_by = 3

class MovieDetail(LoginRequiredMixin, DetailView):
class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    login_url = '/accounts/login/'  
    redirect_field_name = 'movie/movie_detail.html'
    template_name = 'movie/movie_detail.html'
    login_url = '/accounts/login/'  
    redirect_field_name = 'movie/movie_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context

class MovieCategory(LoginRequiredMixin, ListView):
    model = Movie
    paginate_by = 4
    template_name = 'movie/movie_category_list.html'

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
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



