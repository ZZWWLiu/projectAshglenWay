from urllib2 import Request, urlopen
import urllib2, json, os, time

tmdb_api_key = "c8181ac4ae7e7ec434da410e40b8ef12"
now_playing_url = "http://api.themoviedb.org/3/movie/now_playing"


def get_now_playing_movies():
	url = now_playing_url+'?api_key='+tmdb_api_key
	request = Request(url)
	response_body = urlopen(request).read()
	print response_body


if __name__ == '__main__':
	get_now_playing_movies()