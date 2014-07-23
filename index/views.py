from django.shortcuts import render
from index import controller
# Create your views here.
def index(request):
	movies = controller.getMovies()
	return render(request, "index.html", {"movies": movies})


