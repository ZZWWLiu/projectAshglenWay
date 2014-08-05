from django.shortcuts import render

from userProfile import controllers

# Create your views here.
def collectedMovie(request):
	try:
		username = request.session['username']
	except Exception, e:
		print "you have to log in first"
		return redirect("/signin")
	else:
		likedMovies = controllers.get_collected_movies(username)
		likedMoviesTitle = []
		for m in likedMovies:
			likedMoviesTitle.append(m.title)
		return render(request, "userProfile/profile.html", {"movies": likedMovies, "username": username, "likedMovies":likedMoviesTitle})