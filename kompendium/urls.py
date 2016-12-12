from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Topics
    url(r'^topics/$', views.topics, name='topics'),
    # Subtopics
    url(r'^topics/(?P<topic_id>\d+)/$', views.subtopics, name='topic'),
    # Entries
    url(r'^topics/(?P<topic_id>\d+)/(?P<subtopic_id>\d+)/$', views.entry, name='entry'),
    # Links
    url(r'^links/$', views.links, name='links'),
    # US Art
    url(r'^echo/$', views.us_selektion, name='us_selektion'),
    # US Bilderlist
    url(r'^echo/(?P<us_bilderliste_id>\d+)/$', views.us_bilderliste, name='us_bilderliste'),
    # Form Test
    url(r'^rechner/$', views.rechner, name='rechner')
]

