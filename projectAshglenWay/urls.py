from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectAshglenWay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user_profile/', include('userProfile.urls')),
    url(r'^movies/', include('index.urls',namespace='index')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^logsystem/', include('signup.urls')),
    
)
