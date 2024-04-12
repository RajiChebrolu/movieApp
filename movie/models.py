from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
)

LANGUAGE_CHOICES =(
    ('EN', 'ENGLISH'),
    ('KR', 'KOREAN'),
    ('HI', 'HINDI'),
    ('SP', 'SPANISh'),
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies', default='default_image.jpg')
<<<<<<< HEAD
<<<<<<< HEAD
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
=======
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    status = models.CharField(choices=STATUS_CHOICES, max_length=5)
>>>>>>> fb08546 (Changes in the following pages,)
=======
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    status = models.CharField(choices=STATUS_CHOICES, max_length=5)
>>>>>>> 68e5e43 (UPDATE files)
    production_of_year = models.DateField()
    views_count = models.IntegerField(default=0)
    cast = models.CharField(max_length=100)
    


    def __str__(self) -> str:
        return self.title
    
Link_CHOICES =(
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=Link_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return self.movie

class Download_Links(models.Model):
    pass

