from django.shortcuts import render
from index import controllers
# Create your views here.
def index(request):
	movies = controllers.getMovies()
	return render(request, "index.html", {"movies": movies})


def search(request):
	return render(request, "hello world")
