'''
Created on Apr 30, 2015

@author: aix
'''

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#     Examples:
#     url(r'^$', 'DjLoginSystem.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),
#     url(r'^_\d', 'friend.views.friend_home', name='friend_home'),
    url(r'^_(?P<friend_id>.*)', 'friend.views.friend_home', name='friend_home'),
    url(r'^/search', 'friend.views.friend_add', name='friend_add'),
#     url(r'^register/info', 'account.views.info', name='info'),

  )
