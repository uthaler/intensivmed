from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic, Subtopic, Entry, Kategorie, Link, US_Selektion, US_Bilderliste
from .forms import RechnerForm

# Create your views here.

def index(request):
    """ the home page for intensivmed """
    return render(request, 'kompendium/index.html')

def topics(request):
    """ Show all topics """
    topics = Topic.objects.order_by('date_added')
    #topics = Topic.objects.all()
    context = {'topics' : topics}
    return render(request, 'kompendium/topics.html', context)

def subtopics(request, topic_id):
    """ Show subtopics """
    topics = Topic.objects.get(id=topic_id)
    subtopics = topics.subtopic_set.all()
    context = {'topics' : topics, 'subtopics' : subtopics}
    return render(request, 'kompendium/subtopics.html', context)

def entry(request, topic_id, subtopic_id):
    """ Show entry """
    topics = Topic.objects.get(id=topic_id)
    subtopics = Subtopic.objects.get(id=subtopic_id)
    entry = subtopics.entry_set.order_by('-date_added')
    context = {'entry' : entry}
    return render(request, 'kompendium/entries.html', context)

def links(request):
    kategorien = Kategorie.objects.all()
    context = {'kategorien' : kategorien}
    return render(request, 'kompendium/links.html', context)

def us_selektion(request):
    """ Show US links """
    auswahl = US_Selektion.objects.all()
    context = {'auswahl' : auswahl}
    return render(request, 'kompendium/echo.html', context)

def us_bilderliste(request, us_bilderliste_id):
    """ Show pic list """
    bilder_selektion = US_Selektion.objects.get(id=us_bilderliste_id)
    bilder_liste = bilder_selektion.us_bilderliste_set.all()
    context = {'bilder_selektion' : bilder_selektion, 'bilder_liste' : bilder_liste}
    return render(request, 'kompendium/us_bilderliste.html', context)

def rechner(request):
    if request.method != 'POST':
        form = RechnerForm()
    else:
        form = RechnerForm(data=request.POST)
        if form.is_valid():
            natrium = form['natrium'].value()
            kalium = form['kalium'].value()
            print natrium
            print kalium
            def ergebnis(natrium, kalium):
                natrium = int(natrium)
                kalium = int(kalium)
                result = natrium + kalium
                return result
            resultat = ergebnis(natrium, kalium)
            context = {'resultat' : resultat}
            return render(request, 'kompendium/results.html', context)

    context = {'form' : form}
    return render(request, 'kompendium/rechner.html', context)

