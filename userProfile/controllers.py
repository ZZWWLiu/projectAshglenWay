from index.models import Movie, Comment
from signup.models import User

def get_collected_movies(username):
	user = User.objects.get(username = username)
	movies = user.collections.all()
	return movies
