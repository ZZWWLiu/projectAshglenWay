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
		try:
			likedMovies = userProfile.controllers.get_collected_movies(username)
		except Exception, e:
			return render(request, "index.html", {"movies": movies, "username": username, "likedMovies":[]})
		else:
			likedMoviesTitle = []
			for m in likedMovies:
				likedMoviesTitle.append(m.title)
			if movieName:
				controllers.addMovieForUser(username, movieName)
			return render(request, "index.html", {"movies": movies, "username": username, "likedMovies":likedMoviesTitle})


def search(request):
	query = request.POST.get('query')
	search_res = controllers.get_search_res(query)
	try:
		username = request.session['username']
	except KeyError:
		return render(request, "search_res.html", {"search_res":search_res})
	else:
		return render(request, "search_res.html", {"search_res":search_res, "username": username} )

def movie_info(request, id):
	comments = []
	movie_info = controllers.get_movie_info_by_id(id)
	#deal with comments
	print movie_info['title']
	movieName = movie_info['title']

	comments = controllers.getComments(movieName)

	try:
		username = request.session['username']
	except KeyError:
		return render(request, "movie_info.html", {"comments": comments, "movie_info":movie_info})
	else:
		if request.method == 'POST':
			comment = request.POST['comment']
			controllers.addCommentForUser(username, movieName, comment)
		return render(request, "movie_info.html", {"comments": comments, "movie_info":movie_info, "username": username})
