from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.


##################
# NEWS auf Index #
##################

class News(models.Model):
    news_date_added = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    news_text = models.TextField(null=True, blank=True)
    news_image = models.ImageField(upload_to='documents/', null=True, blank=True)
    def __unicode__(self):
        return self.news_text[:20]

###############
# KOMPENDIUM  #
###############

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.text

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.text

class Entry(models.Model):
    subtopic = models.ForeignKey(Subtopic)
    heading_1 = models.CharField(max_length=200, null=True, blank=True)
    heading_2 = models.CharField(max_length=200, null=True, blank=True, default='Epidemiologie')
    heading_3 = models.CharField(max_length=200, null=True, blank=True)
    heading_4 = models.CharField(max_length=200, null=True, blank=True)
    heading_5 = models.CharField(max_length=200, null=True, blank=True)
    heading_6 = models.CharField(max_length=200, null=True, blank=True)
    heading_7 = models.CharField(max_length=200, null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    text7 = models.TextField(null=True, blank=True)
    text8 = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='documents/', null=True, blank=True)
    image2 = models.ImageField(upload_to='documents/', null=True, blank=True)
    image3 = models.ImageField(upload_to='documents/', null=True, blank=True)
    image4 = models.ImageField(upload_to='documents/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.heading_1[:50]

#########
# LINKS #
#########

class Kategorie(models.Model):
    kategorie_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.kategorie_text

class Link(models.Model):
    kategorie = models.ForeignKey(Kategorie, related_name='links')
    link_text = models.URLField(max_length=200)

    def __unicode__(self):
        return self.link_text

###############
# ULTRASCHALL #
###############

class US_Selektion(models.Model):
    selektion_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.selektion_text

class US_Bilderliste(models.Model):
    bilderliste_fk = models.ForeignKey(US_Selektion)
    bilderliste_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bilderliste_text

################################
# Form Hyponatriaemie #
#

# class Calcs(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add = True)

#     def __unicode__(self):
#         return self.text

class Rechner(models.Model):
    BOOL_CHOICES = ((True, 'male'), (False, 'female'))

    natrium = models.PositiveSmallIntegerField('Na+', null=True)
    kalium = models.PositiveSmallIntegerField('K+', null=True)
    alter = models.PositiveSmallIntegerField('Age', null=True)
    geschlecht = models.BooleanField('Gender',choices=BOOL_CHOICES,default=True)
    kg = models.PositiveSmallIntegerField('kg', null=True)
    serumOsmo = models.PositiveSmallIntegerField('S-Osmo', null=True)
    uosmo = models.PositiveSmallIntegerField('U-Osmo', null=True)
    unatrium = models.PositiveSmallIntegerField('U-Na+', null=True)
    blutzucker = models.PositiveSmallIntegerField('Glucose', null=True)
    bun = models.PositiveSmallIntegerField('BUN', null=True)

    def __unicode__(self):
        return (self.natrium, self.kalium, self.alter, self.geschlecht, self.kg, self.serumOsmo, self.uosmo, self.unatrium, self.blutzucker, self.bun)
    

    # auskommentiert ist methode mit @staticmethod (eigentlich einfacher als normale OOP)

    # @staticmethod
    # def calculatedOsmolality(natrium, kalium, blutzucker, bun):
    #             natrium = int(natrium)
    #             kalium = int(kalium)
    #             blutzucker = int(blutzucker)
    #             bun = int(bun)
    #             osmo_result = (2 * (natrium + kalium) + blutzucker /18 + bun / 2.8)
    #             return osmo_result

    def calculatedOsmolality(self, natrium, kalium, blutzucker, bun):
                natrium = int(natrium)
                kalium = int(kalium)
                blutzucker = int(blutzucker)
                bun = int(bun)
                osmo_result = (2 * (natrium + kalium) + blutzucker /18 + bun / 2.8)
                return osmo_result


    # @staticmethod
    # def osmolalGap(serumOsmo, osmo_result):
    #             serumOsmo = int(serumOsmo)
    #             osmo_result = int(osmo_result)
    #             osmo_gap = serumOsmo - osmo_result
    #             return osmo_gap

    def osmolalGap(self, serumOsmo, osmo_result):
        serumOsmo = int(serumOsmo)
        osmo_result = int(osmo_result)
        osmo_gap = serumOsmo - osmo_result
        return osmo_gap

    # @staticmethod
    # def totalBodyWater(alter, geschlecht, kg):
    #     kg = float(kg)
    #     alter = int(alter)

    #     if geschlecht == 'True' and alter < 60:
    #         tbw = kg / 100 * 60
    #     elif geschlecht == 'False' and alter < 60:
    #         tbw = (kg / 100) * 50
    #     elif geschlecht == 'True' and alter >= 60:
    #         tbw = (kg / 100) * 50
    #     else:
    #         tbw = (kg / 100) * 45
    #     return tbw

    def totalBodyWater(self, alter, geschlecht, kg):
        kg = float(kg)
        alter = int(alter)

        if geschlecht == 'True' and alter < 60:
            tbw = kg / 100 * 60
        elif geschlecht == 'False' and alter < 60:
            tbw = (kg / 100) * 50
        elif geschlecht == 'True' and alter >= 60:
            tbw = (kg / 100) * 50
        else:
            tbw = (kg / 100) * 45
        return tbw

###############
# BGA Rechner #
###############
class BGA(models.Model):
    ph = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    bicarbonate = models.DecimalField('HCO3', null=True, max_digits=5, decimal_places=2, blank=True)
    pco_two = models.DecimalField('pCO2', null=True, max_digits=5, decimal_places=2)
    base_excess = models.DecimalField('BE', null=True, max_digits=5, decimal_places=2)
    
    lactate = models.DecimalField('Lactate', null=True, max_digits=5, decimal_places=2)
    sodium = models.DecimalField('Na', null=True, max_digits=5, decimal_places=2)
    potassium = models.DecimalField('K', null=True, max_digits=5, decimal_places=2, blank=True)
    chloride = models.DecimalField('Cl', null=True, max_digits=5, decimal_places=2)
    albumin = models.DecimalField('Albumin', null=True, max_digits=5, decimal_places=2, blank=True)
    phosphate = models.DecimalField('PO4', null=True, max_digits=5, decimal_places=2, blank=True)
    po_two = models.DecimalField('pO2', null=True, max_digits=5, decimal_places=2, blank=True)

    anion_gap = models.DecimalField('Anion gap', null=True, max_digits=5, decimal_places=2)
    ag_albumin_correction = models.DecimalField('Anion gap (corrected for albumin)', null=True, max_digits=5, decimal_places=2)
    
    #Stewart approach
    base_excess_elyte = models.DecimalField('BE electrolytes', null=True, max_digits=5, decimal_places=2)
    base_excess_albumin = models.DecimalField('BE albumin', null=True, max_digits=5, decimal_places=2)
    base_excess_lactate = models.DecimalField('BE lactate', null=True, max_digits=5, decimal_places=2)
    base_excess_uma = models.DecimalField('BE unmeasured anions', null=True, max_digits=5, decimal_places=2)

    #Urine
    chloride_urine = models.DecimalField('U-Cl', null=True, max_digits=5, decimal_places=2, blank=True)
    sodium_urine = models.DecimalField('U-Na', null=True, max_digits=5, decimal_places=2, blank=True)
    potassium_urine = models.DecimalField('U-K', null=True, max_digits=5, decimal_places=2, blank=True)
    urine_SID = models.DecimalField('U-SID', null=True, max_digits=5, decimal_places=2, blank=True)
    urine_ph = models.DecimalField('U-pH', null=True, max_digits=5, decimal_places=2, blank=True)
    
    # expected changes pCO2/HCO3
    met_acid_pco_two_expected = models.DecimalField('Metabolic acidosis pCO2', null=True, max_digits=5, decimal_places=2)
    met_alk_pco_two_expected = models.DecimalField('Metabolic alkalosis pCO2', null=True, max_digits=5, decimal_places=2)
    acute_resp_acid_bicarbonate_expected = models.DecimalField('Acute respiratory acidosis HCO3', null=True, max_digits=5, decimal_places=2)
    chronic_resp_acid_bicarbonate_expected = models.DecimalField('Chronic respiratory acidosis HCO3', null=True, max_digits=5, decimal_places=2)
    chronic_resp_acid_be_expected = models.DecimalField('Chronic respiratory acidosis BE', null=True, max_digits=5, decimal_places=2)
    acute_resp_alk_bicarbonate_expected = models.DecimalField('Acute respiratory alkalosis HCO3', null=True, max_digits=5, decimal_places=2)
    chronic_resp_alk_bicarbonate_expected = models.DecimalField('Chronic respiratory alkalosis HCO3', null=True, max_digits=5, decimal_places=2)
    chronic_resp_alk_be_expected = models.DecimalField('Chronic respiratory alkalosis BE', null=True, max_digits=5, decimal_places=2)

    def pco_two_checker(self, pco_two):
        pco_two = float(pco_two)
        if pco_two < 35:
            pco_two = "Respiratory alkalosis"
        elif pco_two > 45:
            pco_two = "Respiratory acidosis"
        else:
            pco_two = "Normal"
        return pco_two

    def be_checker(self, base_excess):
        base_excess = float(base_excess)
        if base_excess < -2:
            base_excess = "Metabolic acidosis"
        elif base_excess > 2:
            base_excess = "Metabolic alkalosis"
        else:
            base_excess = "Normal"
        return base_excess

    def ph_checker(self, ph):
        ph = float(ph)
        if ph < 7.35:
            ph = "Acidemia"
        elif ph > 7.45:
            ph = "Alkalemia"
        else:
            ph = "No acidemia/alkalemia"
        return ph

    def be_subsets_na(self, sodium):
        sodium = float(sodium)
        be_na = 0.3 * (sodium - 142.5)
        return be_na

    def be_subsets_cl(self, chloride, sodium):
        chloride = float(chloride)
        sodium = float(sodium)
        be_cl = 102.5 - ((chloride / sodium) * 142.5)
        return be_cl

    def be_subsets_alb(self, albumin, ph):
        if not albumin:
            return
        albumin = float(albumin)
        ph = float(ph)
        be_alb = (0.148 * ph - 0.818) * (42.5 - albumin)
        return be_alb

    def be_subsets_lact(self, lactate):
        lactate = float(lactate)
        be_lact = 1 - lactate
        return be_lact

    def be_subsets_uma(self, base_excess, be_na, be_cl, be_alb, be_lact):
        if not be_alb:
            return
        base_excess = float(base_excess)
        be_na = float(be_na)
        be_cl = float(be_cl)
        be_alb = float(be_alb)
        be_lact = float(be_lact)
        be_uma = base_excess - be_na - be_cl - be_alb - be_lact
        return be_uma

    def be_diagnosis_na(self, be_na):
        be_na = float(be_na)
        if be_na < -2:
            be_na = "Hyponatremic acidosis"
        elif be_na > 2:
            be_na = "Hypernatremic alkalosis"
        else:
            be_na = "No relevant Na+ effect"
        return be_na

    def be_diagnosis_cl(self, be_cl):
        be_cl = float(be_cl)
        if be_cl < -2:
            be_cl = "Hyperchloremic acidosis"
        elif be_cl > 2:
            be_cl = "Hypochloremic alkalosis"
        else:
            be_cl = "No relevant Cl- effect"
        return be_cl

    def be_diagnosis_alb(self, be_alb):
        if not be_alb:
            return
        be_alb = float(be_alb)
        if be_alb < -2:
            be_alb = "Hyperalbuminemia acidosis"
        elif be_alb > 2:
            be_alb = "Hypoalbuminemia alkalosis"
        else:
            be_alb = "No relevant albumin effect"
        return be_alb

    def be_diagnosis_lact(self, be_lact):
        be_lact = float(be_lact)
        if be_lact < -2:
            be_lact = "Lactic acidosis"
        else:
            be_lact = "No relevant lactate effect"
        return be_lact

    def be_diagnosis_uma(self, be_uma):
        if not be_uma:
            return
        be_uma = float(be_uma)
        if be_uma < -2:
            be_uma = "unmeasured anions acidosis"
        else:
            be_uma = "No relevant unmeasured anions effect"
        return be_uma



####### HYPERCHLORAEMISCHE AZIDOSE ###
    def hyperchlor_acidosis_patho(self):
        hyperchlor_acidosis_patho = "<table><tr><th>impaired H+ elimination</th></tr><tr><td>RTA, renal failure, hypoaldosteronism</td></tr><tr><th>enteral HCO3- loss</th><tr><td>diarrhoea, pancreatic- or duodenal drainage, urinary fistula, cholestyramin</td></tr></tr><tr><th>acid gain</th><tr><td>hyperalimentation, cristalloid / colloids with high Cl- concentration, rhabdomyolysis</td></tr><tr><td>counterregulation for respiratory alkalosis incl. post-hypocapnic-acidosis</td></tr></table>"
        return hyperchlor_acidosis_patho

    def hyperchlor_acidosis(self, sodium_urine, potassium_urine, chloride_urine):
        if not sodium_urine:
            return "Urinary anion gap cannot be calculated: missing value"
        if not potassium_urine:
            return "Urinary anion gap cannot be calculated: missing value"
        if not chloride_urine:
            return "Urinary anion gap cannot be calculated: missing value"
        su = float(sodium_urine)
        pu = float(potassium_urine)
        cu = float(chloride_urine)
        uag = (su + pu) - cu
        uag = str(uag)
        urinary_ag = "Urinary anion gap: " + uag + " (U-Na + U-K - U-Cl)"
        return urinary_ag

    def hyperchlor_acidosis_uag(self, sodium_urine, potassium_urine, chloride_urine):
        if not sodium_urine:
            return ""
        if not potassium_urine:
            return ""
        if not chloride_urine:
            return ""
        su = float(sodium_urine)
        pu = float(potassium_urine)
        cu = float(chloride_urine)
        urinary_ag = (su + pu) - cu
        if urinary_ag < 0:
            hyperchlor_acidosis_result = "Urinary AG negative: Extrarenal HCO3 loss, Acid gain."
        else:
            hyperchlor_acidosis_result = "Urinary AG positive: RTA, renal failure GFR < 60."
        return hyperchlor_acidosis_result

    def hyperchlor_acidosis_rta(self, urinary_ag, potassium, urine_ph):
        if not urinary_ag:
            return ""
        if not potassium:
            return ""
        if not urine_ph:
            return ""
        urinary_ag = float(urinary_ag)
        potassium = float(potassium)
        urine_ph = float(urine_ph)
        if urinary_ag > 0:
            if potassium > 3.5 or potassium < 5 or potassium < 3.5:
                if urine_ph > 5.5:
                    rta = "RTA 1 classic: post NTX, SLE, Sjoegren syndrome"
                else:
                    rta = "RTA 2: Fanconi syndrome, myeloma, acetazolamide"
            elif potassium > 5:
                if urine_ph > 5.5:
                    rta = "RTA 1 hyperkalemic: obstructive uropathy, amiloride"
                else:
                    rta = "RTA 4: diabetes, chronic renal failure, ACEI, NSAR, spironolactone"
        else:
            return ""
        return rta


####### HYPOCHLORAEMISCHE ALKALOSE ###

    def hypochlor_alkalosis_patho(self):
        hypochlor_alkalosis_patho = "<table><tr><th>H+ loss</th></tr><tr><td>GI loss: vomiting, loss via gastric tube, diarrhoea</td></tr><tr><td>Renal loss: diuretics, hypokalemia, post hypercapnic alkalosis, prim. hyperaldosteronism, hypercortisolism, hypercalcemia, penicillin, Liddle-Syndrom</td></tr><tr><td>secondary hyperaldosteronism: heart failure, liver failure, chronic hypoxemia, renal artery stenosis, Barrter syndrome, Gitelman syndrome</td></tr><tr><th>H+ shift</th><tr><td>hypokalemia, refeeding syndrome</td></tr></tr><tr><th>HCO3 retention</th><tr><td>contraction alkalosis due to fluid loss, reaction to respiratory acidosis</td></tr><tr><th>HCO3 gain</th></tr><tr><td>citrat in blood transfusion, lacate / acetate in cristalloids</td></tr></table>"
        return hypochlor_alkalosis_patho

    def hypochlor_alkalosis_cl(self, chloride_urine):
        if not chloride_urine:
            return ""
        chloride = float(chloride_urine)
        if chloride < 20:
            chloride = "<table><tr>chloride responsive (U-Cl < 20 mmol/l)</tr><tr></tr><tr><td>eins</td><td>zwei</td></tr></table>"
        else:
            chloride = "chloride unresponsive (U-Cl > 20 mmol/l)"
        return chloride

    def check_ph(self, ph, pco_two, bicarbonate, base_excess):
        ph = float(ph)
        base_excess = float(base_excess)
        pco_two = float(pco_two)
        if ph < 7.35 and base_excess < -2:
             ph_text = "Metabolic acidosis"
        elif ph < 7.35 and pco_two > 45 and base_excess > -2 and base_excess < 2:
            ph_text = "Acute respiratory acidosis"
        elif ph < 7.35 and pco_two > 45 and base_excess > 2:
            ph_text ="Chronic respiratory acidosis"
        elif ph > 7.45 and base_excess > 2:
            ph_text = "Metabolic Alkalosis"
        elif ph > 7.45 and pco_two < 35 and base_excess > -2 and base_excess < 2:
            ph_text = "Acute respiratory alkalosis"
        elif ph > 7.45 and pco_two < 35 and base_excess < -2:
            ph_text = "Chronic respiratory alkalosis"
        else:
            ph_text = "nix"
        return ph_text


############ TRADITIONAL APPROACH ########################

    def anion_gap(self, sodium, bicarbonate, chloride):
        if not sodium:
            return "Anion gap cannot be calculated: missing value"
        if not bicarbonate:
            return "Anion gap cannot be calculated: missing value"
        if not chloride:
            return "Anion gap cannot be calculated: missing value"
        sodium = float(sodium)
        bicarbonate = float(bicarbonate)
        chloride = float(chloride)
        anion_gap = sodium - (bicarbonate + chloride)
        return anion_gap

    def albumin_adjust(self, albumin, phosphate):
        if not albumin:
            return "Anion gap albumin adjusted cannot be calculated: missing value"
        if not phosphate:
            return "Anion gap albumin adjusted cannot be calculated: missing value"
        albumin = float(albumin)
        phosphate = float(phosphate)
        albumin_adjust = 0.2 * albumin + 1.5 * phosphate
        return albumin_adjust

    def expected_results(self, ph, pco_two, bicarbonate, base_excess):
        ph = float(ph)
        pco_two = float(pco_two)
        bicarbonate = float(bicarbonate)
        base_excess = float(base_excess)
        if ph < 7.35 and base_excess <-2:
            expected_pco_two = 40 + base_excess
            ergebnis = "Expected pCO2 is: " + str(expected_pco_two)
        elif ph < 7.35 and pco_two > 45 and base_excess > -2 and base_excess < 2:
            expected_bicarbonate = ((pco_two - 40) / 10) + 24
            ergebnis = "Expected HCO3 is: " + str(expected_bicarbonate)
        else:
            ergebnis = pco_two
        return ergebnis

        #da passt was nicht
    # def checker(self, expected_results, bicarbonate):
    #     expected_results = float(expected_results)
    #     bicarbonate = float(bicarbonate)
    #     #acute respiratory acidosis
    #     if bicarbonate > expected_results:
    #         checker_ergebnis = "Additional metabolic disorder."
    #     return checker_ergebnis

#############
# EDIC      # 
#############

class EDIC(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.text
