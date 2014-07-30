from django.db import models
from django import forms
from index.models import Movie


class SignUpForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)
	confirm_password = forms.CharField(max_length = 20)

class SignInForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	collections = models.ManyToManyField(Movie)
	
	def __unicode__(self):
		return self.username
		

