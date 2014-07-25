from django.shortcuts import render
from index import controllers
# Create your views here.
def index(request):
	movies = controllers.getMovies()
	return render(request, "index.html", {"movies": movies})


def search(request):
	query = request.POST.get('query')
	search_res = controllers.get_search_res(query)
	return render(request, "search_res.html", {"search_res":search_res})
