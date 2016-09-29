"""palestra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', 'tchelinux2016.views.sobre'),
    url(r'^wbg/', 'tchelinux2016.views.sobrewbg'),
    url(r'^prints/([0-9]+)/$', 'tchelinux2016.views.prints'),
    url(r'^prints_wbg/([0-9]+)/$', 'tchelinux2016.views.printswbg'),
    url(r'^fontes/', 'tchelinux2016.views.fontes'),
    url(r'^fontes_wbg/', 'tchelinux2016.views.fonteswbg'),
    url(r'^conclusao/', 'tchelinux2016.views.conclusao'),
    url(r'^conclusao_wbg/', 'tchelinux2016.views.conclusaowbg'),

#    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
        urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )
                
