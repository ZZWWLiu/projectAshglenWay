from django.shortcuts import render
from index import controllers
import userProfile
# Create your views here.
def index(request):
	movies = controllers.get_now_playing_movies()
	movieName = request.GET.get('movie')
	try:
		username = request.session['username']
	except KeyError:
		if movieName:
			print "sorry you have to log in first"
		return render(request, "index.html", {"movies": movies})
	else:
		likedMovies = userProfile.controllers.get_collected_movies(username)
		likedMoviesTitle = []
		for m in likedMovies:
			likedMoviesTitle.append(m.title)
		if movieName:
			controllers.addMovieForUser(username, movieName)
		return render(request, "index.html", {"movies": movies, "username": username, "likedMovies":likedMoviesTitle})


def search(request):
	query = request.POST.get('query')
	search_res = controllers.get_search_res(query)
	return render(request, "search_res.html", {"search_res":search_res})

def movie_info(request, id):
	movie_info = controllers.get_movie_info_by_id(id)
	return render(request, "movie_info.html", {"movie_info":movie_info})