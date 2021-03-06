from django.shortcuts import render
from django.shortcuts import render_to_response
from signup import controller
from signup.models import SignUpForm, SignInForm
from django.shortcuts import redirect
from time import sleep
from signup.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm




# Create your views here.
def register(request):
	errors = []
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		print dir(form)
		if form.is_valid():
			
			cd = form.cleaned_data
			username = cd['username']
			password = cd['password']
			print password
			confirm_password = cd['confirm_password']
			if controller.exist_username(username):
				errors.append("username already be taken")
			if not controller.valid_username(username):
				errors.append("username should be digits and letters combination!")
			if not controller.valid_password(password):
				errors.append("password should be more than 8 letters")
			if (confirm_password != password):
				errors.append("confrim_password should be same as password")
			if not errors:
				user = User(username = username, password = password)
				user.save()
				request.session['username'] = user.username
				return redirect('welcome')
		else:
				errors.append("You need to type in both your username and password!")
	return render(request, 'signup.html', {'errors' : errors})

def signin(request):
	errors = []
	#userlist = []
	if request.method == 'POST':
		form2 = SignInForm(request.POST)
		if form2.is_valid():
			cd = form2.cleaned_data
			username = cd['username']
			password = cd['password']
			try:
				u = User.objects.get(username = username)
			except User.DoesNotExist:
				errors.append("This username is not exist")
			else:
				if (u.password == password):
					request.session['username'] = username
					return redirect('welcome')
				else:
					errors.append("Your password is not match with your username")
		else:
			errors.append("You need to type in username and password!")
	return render(request, 'signin.html', {'errors': errors})



def welcome(request):
	username = request.session['username']
	return render(request, 'welcome.html', {'username':username})
	#sleep(2)
	#return redirect('/')


def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return redirect('/movies')