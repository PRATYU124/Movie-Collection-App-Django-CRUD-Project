from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    return render(request, 'movieapp/index.html')

def add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_movies')  # Redirect to movie list after add
    else:
        form = MovieForm()
    return render(request, 'movieapp/addmovie.html', {'form': form})

def list_movies(request):
    hero_query = request.GET.get('hero', '')
    if hero_query:
        movies = Movie.objects.filter(hero__icontains=hero_query)
    else:
        movies = Movie.objects.all()
    
    return render(request, 'movieapp/listmovie.html', {'movies': movies})
