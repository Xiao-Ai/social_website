'''
Created on Apr 26, 2015

@author: aix
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#     Examples:
#     url(r'^$', 'DjLoginSystem.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),
    url(r'^$', 'publish.views.status', name='status'),
    
  )
