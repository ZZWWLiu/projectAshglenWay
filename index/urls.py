from django.conf.urls import patterns, url

from index import views

urlpatterns = patterns(
	'',
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^id=(?P<id>\d+)$', 'index.views.movie_info'),
)