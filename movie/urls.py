from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import MovieList, MovieDetail, SignUpView  # Import SignUpView from your views

app_name = 'movies'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='movies:login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),  # Use the SignUpView from your views
]


# At the moment is not implemented categories

# app_name='movie'
# urlpatterns = [
#     path('', MovieList.as_view(), name='movie_list'),
#     path('category/<str:category>', MovieCategory.as_view(), name='movie_category'), 
#     path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
# ]




