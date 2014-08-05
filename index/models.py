from django.db import models
#from signup.models import SignUpForm
# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length = 20)
	poster_path = models.CharField(max_length = 200, blank = True, null= True)
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	username =models.CharField(max_length = 20)
	content = models.TextField(max_length = 500)
	movie = models.ForeignKey(Movie)
	created_time = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.content