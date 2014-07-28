from django.shortcuts import render
from index import controllers
# Create your views here.
def index(request):
	

	movies = controllers.get_now_playing_movies()
	try:
		username = request.session['username']
	except KeyError:
		return render(request, "index.html", {"movies": movies})
	else:
		movieName = request.GET.get('movie')
		print movieName
		if movieName:
			controllers.addMovieForUser(username, movieName)
		return render(request, "index.html", {"movies": movies, "username": username})


def search(request):
	query = request.POST.get('query')
	search_res = controllers.get_search_res(query)
	return render(request, "search_res.html", {"search_res":search_res})

# def like(request):
# 	movie = request.POST.get("movie")
# 	print movie
# 	return render(request, "search_res.html")