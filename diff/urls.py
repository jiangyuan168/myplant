from django.conf.urls import url
from . import views

app_name = 'diff'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^register/$', views.register, name='register'),
    url(r'^channel/(?P<cid>[0-9]+)/$', views.ChannelView.as_view(), name='channel'),
    #url(r'^channel/(?P<cid>[0-9]+)/$', views.channel, name='channel'),
]
