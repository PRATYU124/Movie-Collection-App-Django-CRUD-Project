from django import forms
from .models import Movie  # Ensure the path to Movie is correct

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
