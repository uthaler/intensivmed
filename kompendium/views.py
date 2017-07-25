from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Topic, Subtopic, Entry, Kategorie, Link, US_Selektion, US_Bilderliste, News, EDIC, Rechner, BGA
from .forms import RechnerForm, BGAForm

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
    bga = "BGA"
    context = {'calcs' : calcs, 'bga' : bga}
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
            
            # auskommentiert ist einfachere methode mit @staticmethod
            a = Rechner()
            osmo_result = a.calculatedOsmolality(natrium, kalium, blutzucker, bun)
            #osmo_result = Rechner.calculatedOsmolality(natrium, kalium, blutzucker, bun)
            osmo_gap = a.osmolalGap(serumOsmo, osmo_result)
            #osmo_gap = Rechner.osmolalGap(serumOsmo, osmo_result)
            tbw = a.totalBodyWater(alter, geschlecht, kg)

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

def bga(request):
    if request.method != 'POST':
        form = BGAForm()
    else:
        form = BGAForm(data=request.POST)
        if form.is_valid():
            ph = form.cleaned_data['ph']
            pco_two = form.cleaned_data['pco_two']
            bicarbonate = form.cleaned_data['bicarbonate']
            base_excess = form.cleaned_data['base_excess']
            sodium = form.cleaned_data['sodium']
            chloride = form.cleaned_data['chloride']
            albumin = form.cleaned_data['albumin']
            phosphate = form.cleaned_data['phosphate']
            lactate = form.cleaned_data['lactate']
            sodium_urine = form['sodium_urine'].value()
            potassium_urine = form['potassium_urine'].value()
            chloride_urine = form['chloride_urine'].value()
            potassium = form['potassium'].value()
            urine_ph = form['urine_ph'].value()

            names = [ph, pco_two, bicarbonate, base_excess]

            x = BGA()

            pco_two_result = x.pco_two_checker(pco_two)
            be_result = x.be_checker(base_excess)
            ph_result = x.ph_checker(ph)
            
            # STEWART APPROACH #
            
            be_na = x.be_subsets_na(sodium)
            be_cl = x.be_subsets_cl(chloride, sodium)
            be_alb = x.be_subsets_alb(albumin, ph)
            be_lact = x.be_subsets_lact(lactate)
            be_uma = x.be_subsets_uma(base_excess, be_na, be_cl, be_alb, be_lact)
            be_na_diagnosis = x.be_diagnosis_na(be_na)
            be_cl_diagnosis = x.be_diagnosis_cl(be_cl)
            be_alb_diagnosis = x.be_diagnosis_alb(be_alb)
            be_lact_diagnosis = x.be_diagnosis_lact(be_lact)
            be_uma_diagnosis = x.be_diagnosis_uma(be_uma)
            

            ### hyperchloremic acidosis ####
            hyperchlor_acidosis_patho = x.hyperchlor_acidosis_patho()
            hyperchlor_acidosis = x.hyperchlor_acidosis(sodium_urine, potassium_urine, chloride_urine)
            hyperchlor_acidosis_uag = x.hyperchlor_acidosis_uag(sodium_urine, potassium_urine, chloride_urine)
            rta = x.hyperchlor_acidosis_rta(hyperchlor_acidosis, potassium, urine_ph)
            
            ### hypochloraemische azidose ###
            hypochlor_alkalosis_patho = x.hypochlor_alkalosis_patho()
            hypochlor_alkalosis_cl = x.hypochlor_alkalosis_cl(chloride_urine)

            #traditional approach
            anion_gap = x.anion_gap(sodium, bicarbonate, chloride)
            albumin_adjust = x.albumin_adjust(albumin, phosphate)
            #check_ph = x.check_ph(ph, pco_two, bicarbonate, base_excess)
            #expected_results = x.expected_results(ph, pco_two, bicarbonate, base_excess)
            #checker_ergebnis = x.checker(bicarbonate, expected_results)

            #if check_ph == "Metabolic acidosis":
            #    anion_gap = x.anion_gap(sodium, bicarbonate, chloride)
            #    albumin_adjust = x.albumin_adjust(albumin, phosphate)
            #else:
            #    anion_gap = 0
            #    albumin_adjust = 0

            #context = {'names' : names, 'check_ph' : check_ph, 'expected_results' : expected_results, 'anion_gap' : anion_gap, 'albumin_adjust' : albumin_adjust}
            context = {'names' : names, 'pco_two_result' : pco_two_result, 'be_result' : be_result, 'ph_result' : ph_result, 'be_na' : be_na, 'be_cl' : be_cl, 'be_lact' : be_lact, 'be_alb' : be_alb, 'be_uma' : be_uma, 'anion_gap' : anion_gap, 'albumin_adjust' : albumin_adjust, 'be_na_diagnosis' : be_na_diagnosis, 'be_cl_diagnosis' : be_cl_diagnosis, 'be_alb_diagnosis' : be_alb_diagnosis, 'be_lact_diagnosis' : be_lact_diagnosis, 'be_uma_diagnosis' : be_uma_diagnosis, 'hyperchlor_acidosis' : hyperchlor_acidosis, 'hyperchlor_acidosis_uag' : hyperchlor_acidosis_uag, 'hypochlor_alkalosis_cl' : hypochlor_alkalosis_cl, 'rta' : rta, 'hypochlor_alkalosis_patho' : hypochlor_alkalosis_patho, 'hyperchlor_acidosis_patho' : hyperchlor_acidosis_patho}
            return render(request, 'kompendium/bga_result.html', context)

    context = {'form' : form}
    return render(request, 'kompendium/bga_calc.html', context)


def edic(request):
    text = EDIC.objects.all()
    context = {'text' : text}
    return render(request, 'kompendium/edic.html', context)

