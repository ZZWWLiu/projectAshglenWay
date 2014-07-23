rtAPI_KEY = "8a6jr5tht3npp8u3m6tcktfk"
rtBaseURL = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey="+rtAPI_KEY+"&page_limit=1&q="

tsm_apikey = "3x3ceywr4k4dy7npqrdvyd5t"

baseURL = "http://data.tmsapi.com/v1/movies/showings?"

moviefile = "movies.json"
moviefile2 = "movies2.json"

# http://data.tmsapi.com/v1/movies/showings?startDate=2014-07-21&zip=95133&api_key=3x3ceywr4k4dy7npqrdvyd5t
from datetime import datetime
import urllib2, json, os, time
import pprint

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


def getData(baseurl, api_key, date, zipcode):
	url = baseurl+"startDate="+date+"&zip="+zipcode+"&api_key="+api_key
	urlfile = urllib2.urlopen(url)
	data = json.loads(urlfile.read())
	urlfile.close()
	return data

def getImageUrl(baseurl, movieName):
	name = movieName.replace(" ", "+")
	url = baseurl+name
	print url
	urlfile = urllib2.urlopen(url)
	data = json.loads(urlfile.read())
	urlfile.close()
	if data["total"] == 1:
		return data["movies"][0]["posters"]["detailed"]
	else:
		return ""

def savefile(filename, data):
	jFile = open(filename, 'w')
	jFile.write(json.dumps(data))
	jFile.close()

def getMovies():
	module_dir = os.path.dirname(__file__)  # get current directory
	filename = os.path.join(module_dir, moviefile2)
	data = readJSON(filename)
	return data



if __name__ == '__main__':
	# date = datetime.now().strftime('%Y-%m-%d')
	# data = getData(baseURL, tsm_apikey, date, "95133")
	# pprint.pprint(data)
	# savefile(moviefile, data)

	# read data(get title, img src, description, rating, genre...), and pass it to views
	movies = readJSON(moviefile)
	for movie in movies:
		# print rtBaseURL+movie["title"]
		imgUrl = getImageUrl(rtBaseURL ,movie["title"])
		print movie["title"]
		print imgUrl
		time.sleep(0.2)
		movie["img"] = imgUrl
		pprint.pprint(movie)
	savefile(moviefile2, movies)
