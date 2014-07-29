from urllib2 import Request, urlopen, quote
import urllib2, json, os, time
import pprint
from signup.models import User
from index.models import Movie, Comment


# global varibles
tmdb_api_key = "c8181ac4ae7e7ec434da410e40b8ef12"
now_playing_url = "http://api.themoviedb.org/3/movie/now_playing"
search_url = "http://api.themoviedb.org/3/search/movie"
# filename
moviefile = "movies.json"

def addMovieForUser(username, movieName):
	'''
		if already liked this movie, unlike it (delete it from the db)
	'''
	user = User.objects.get(username = username)
	try:
		movie = Movie.objects.get(title=movieName)
	except Exception, e:
		movie = Movie(title=movieName)
		movie.save()

	try:
		m = user.collections.get(title=movie.title)
	except Exception, e:
		# movie not in the collect, so add to it
		user.collections.add(movie)
	else:
		# movie already in the collect, so exclude from it
		user.collections.remove(movie)
	

def get_now_playing_movies():
	url = now_playing_url+'?api_key='+tmdb_api_key
	headers = {
		'Accept': 'application/json'
	}
	request = Request(url, headers = headers)
	response_body = urlopen(request).read()
	data = json.loads(response_body)
	return data["results"]

def get_movie_info_by_id(id):
	movie_id = id
	url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+tmdb_api_key
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
   	the_page = response.read()
   	result = json.loads(the_page)
	return result

def get_search_res(query):
    moviename = quote(query)
    url = search_url+'?api_key='+tmdb_api_key+'&query='+moviename
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    result = json.loads(the_page)
    return result["results"]

'''
   for test use functions
'''

def readJSON(filename):
    """
    Used to read all data from the json file.
    """
    try:
        with open(filename) as f:
            for line in f:
                data = json.loads(line.strip())
    except:
        print "Failed to read data!"
        return []
    print "The json file has been successfully read!"
    return data

def savefile(filename, data):
	jFile = open(filename, 'w')
	jFile.write(json.dumps(data))
	jFile.close()

def getMovies():
	module_dir = os.path.dirname(__file__)  # get current directory
	filename = os.path.join(module_dir, moviefile)
	data = readJSON(filename)
	return data





if __name__ == '__main__':
	# data = get_now_playing_movies()
	# savefile(moviefile, data)
	movies = getMovies()
	for movie in movies:
		print movie['poster_path']








