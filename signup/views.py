from django.shortcuts import render
from signup import controller

def index(request):
	return render(request, 'signup.html');

# Create your views here.
