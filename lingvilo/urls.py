"""lingvilo URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from portuguese.views import conjugate_pt, subjunctive_constructs, my_vocabulary, can_i_read_this

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portuguese/conjugate/$', conjugate_pt),
    url(r'^portuguese/subjunctive/$', subjunctive_constructs),
    url(r'^portuguese/vocabulary/$', my_vocabulary),
    url(r'^portuguese/canireadthis/$', can_i_read_this),
]
