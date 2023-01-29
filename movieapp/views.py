from django.shortcuts import render
from movieapp import forms
from movieapp.models import Movie


# Create your views here.

def index(request):
    return render(request, 'movieapp/index.html')


def name(request):
    form = forms.Movieform()
    if request.method == 'POST':
        form = forms.Movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index(request)

    return render(request, 'movieapp/name.html', {'form': form})


def list(request):
    movielist = Movie.objects.all()
    return render(request, 'movieapp/list.html', {'movielist': movielist})


def pic(request):
    return render(request, 'movieapp/pic.html')
