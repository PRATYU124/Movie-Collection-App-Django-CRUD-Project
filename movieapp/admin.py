from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('moviename', 'hero', 'heroine', 'rdate')
    search_fields = ('moviename', 'hero')
    list_filter = ('rdate',)
