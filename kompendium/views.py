from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Topic, Subtopic, Entry, Kategorie, Link, US_Selektion, US_Bilderliste, News, EDIC, Rechner
from .forms import RechnerForm

# Create your views here.

def index(request):
    """ the home page for intensivmed """
    news_list = News.objects.order_by('-news_date_added')
    #news_list = News.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 3)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'news' : news}
    return render(request, 'kompendium/index.html', context)

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

def calcs(request):
    """ Show all calculators """
    calcs = "Hyponatremia"
    context = {'calcs' : calcs}
    return render(request, 'kompendium/calcs.html', context)

def rechner(request):
    if request.method != 'POST':
        form = RechnerForm()
    else:
        form = RechnerForm(data=request.POST)
        if form.is_valid():
            natrium = form['natrium'].value()
            kalium = form['kalium'].value()
            blutzucker = form['blutzucker'].value()
            bun = form['bun'].value()
            serumOsmo = form['serumOsmo'].value()
            alter = form['alter'].value()
            geschlecht = form['geschlecht'].value()
            kg = form['kg'].value()
            uosmo = form['uosmo'].value()
            unatrium = form['unatrium'].value()
            
            osmo_result = Rechner.calculatedOsmolality(natrium, kalium, blutzucker, bun)
            osmo_gap = Rechner.osmolalGap(serumOsmo, osmo_result)
            tbw = Rechner.totalBodyWater(alter, geschlecht, kg)

            if osmo_gap > 10:
                osmo_warning = "increased Osmo gap. MAEDIE: methanole, acetone, ethanol, diuretics, ispropanolol, ethylene glycol"
            else:
                osmo_warning = ""

            if int(uosmo) < 100:
                uosmo_warning = "Water excess. Consider primary polydipsia, low solute intake, beer potomania."
            else:
                uosmo_warning = ""

            if int(unatrium) < 30:
                unatrium_warning = "Low effective arterial blood volume. ECF expanded: heart failure, liver failure, nephrotic syndrome. ECF reduced: diarrhea, vomiting, third spacing, remote diuretics."
            else:
                unatrium_warning = ""

            context = {'unatrium_warning' : unatrium_warning, 'uosmo_warning' : uosmo_warning, 'osmo_warning' : osmo_warning, 'natrium' : natrium, 'serumOsmo' : serumOsmo, 'uosmo' : uosmo, 'unatrium' : unatrium, 'osmo_result' : osmo_result, 'osmo_gap' : osmo_gap, 'tbw' : tbw}
            return render(request, 'kompendium/results.html', context)

    context = {'form' : form}
    return render(request, 'kompendium/rechner.html', context)

def edic(request):
    text = EDIC.objects.all()
    context = {'text' : text}
    return render(request, 'kompendium/edic.html', context)

