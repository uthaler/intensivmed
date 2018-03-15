from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Home page Blog mit tags
    url(r'^tagspage/(?P<pk>\d+)/$', views.tagspage, name='tagspage'),
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
    # Calculators
    url(r'^calcs/$', views.calcs, name='calcs'),
        # Hyponatriaemie
    url(r'^calcs/hyponatremia$', views.rechner, name='rechner'),
        # BGA
    url(r'^calcs/bga$', views.bga, name='bga'),
    # EDIC
    url(r'^edic/$', views.edic, name='edic'),
] 


#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    