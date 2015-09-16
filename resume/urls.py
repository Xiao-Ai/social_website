'''
Created on Apr 29, 2015

@author: aix
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#     Examples:
#     url(r'^$', 'DjLoginSystem.views.home', name='home'),
#     url(r'^blog/', include('blog.urls')),
    url(r'^$', 'resume.views.resume', name='resume'),
    url(r'^resume_edu/', 'resume.views.resume_edu', name='resume_edu'),
    url(r'^resume_exp/', 'resume.views.resume_exp', name='resume_exp'),
    url(r'^job_offer/', 'resume.views.job_offer', name='job_offer'),
    
  )