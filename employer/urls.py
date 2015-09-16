'''
Created on May 2, 2015

@author: aix
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#     Examples:
#     url(r'^$', 'DjLoginSystem.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),
    url(r'^$', 'employer.views.login', name='login'),
    url(r'^home/', 'employer.views.home', name='home'),
    url(r'^register/', 'employer.views.register', name='register'),
    url(r'^post/', 'employer.views.post', name='post'),
    url(r'^job_(?P<job_id>.*)', 'employer.views.job', name='job'),
    url(r'^jobs_all/$', 'employer.views.jobs_all', name='jobs_all'),
    url(r'^hired/$', 'employer.views.hired', name='hired'),
  )
