'''
Created on Apr 19, 2015

@author: aix
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#     Examples:
#     url(r'^$', 'DjLoginSystem.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),
      url(r'^$', 'account.views.login', name='home'),
      url(r'^register/$', 'account.views.register', name='register'),
      url(r'^login/$', 'account.views.login', name='login'),
      url(r'^register/info', 'account.views.info', name='info'),
#       url(r'^', 'account.views.homepage', name='homepage'),
  )
