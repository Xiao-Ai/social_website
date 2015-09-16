from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usertest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^status/', include('publish.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^friend', include('friend.urls')),
    url(r'^employer/', include('employer.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)