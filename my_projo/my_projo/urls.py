from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', 'my_projo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^pols/', include('pols.urls')),
   #  url(r'^polls/', include('polls.urls')),
   #  url(r'^pollz/', include('pollz.urls')),
)
