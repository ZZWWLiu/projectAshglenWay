from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns('',
	url(r'signup/$', views.register, name = 'signup'),
	url(r'signup/welcome/', views.welcome, name = 'welcome'),
	# url(r'signin/welcome/', views.welcome, name = 'welcome'),
	url(r'signin/', views.signin, name = 'signin'),
	url(r'logout/', views.logout, name = 'logout'),
)