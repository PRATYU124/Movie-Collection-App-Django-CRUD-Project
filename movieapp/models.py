from django.db import models

class Movie(models.Model):
    moviename = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    heroine = models.CharField(max_length=100)
    rdate = models.DateField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.moviename
