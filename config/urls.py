from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', 'portal.views.index', name='index'),
    url(r'^admin/', admin.site.urls),
]

