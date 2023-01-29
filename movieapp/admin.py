from django.contrib import admin
from movieapp.models import Movie

# Register your models here.


class Moviedisplay(admin.ModelAdmin):
    list_display = ['Mname', 'Dname', 'Rdate']


admin.site.register(Movie, Moviedisplay)
