from django.db import models

# Create your models here.


'''
each movie has multiple comments, but each Comment belongs to one movie
'''

class Movie(models.Model):
	title = models.CharField(max_length = 20)
	# blank=True
	# comments = models.ManyToManyField(Comment)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	content = models.CharField(max_length = 500)
	movie = models.ForeignKey(Movie)
	def __unicode__(self):
		return self.content
	# content , username, time, which movie