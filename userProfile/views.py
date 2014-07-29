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
		movies = controllers.get_collected_movies(username)
		print movies
		return render(request, "profile.html", {"movies": movies})