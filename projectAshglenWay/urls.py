from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectAshglenWay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('index.urls')),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^signup/', include('signup.urls')),
=======
>>>>>>> 099d519d8c270db39baea360c01c46673e30efd7
)
