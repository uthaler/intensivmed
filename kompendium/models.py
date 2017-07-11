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
    
    @staticmethod
    def calculatedOsmolality(natrium, kalium, blutzucker, bun):
                natrium = int(natrium)
                kalium = int(kalium)
                blutzucker = int(blutzucker)
                bun = int(bun)
                osmo_result = (2 * (natrium + kalium) + blutzucker /18 + bun / 2.8)
                return osmo_result

    @staticmethod
    def osmolalGap(serumOsmo, osmo_result):
                serumOsmo = int(serumOsmo)
                osmo_result = int(osmo_result)
                osmo_gap = serumOsmo - osmo_result
                return osmo_gap

    @staticmethod
    def totalBodyWater(alter, geschlecht, kg):
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

  

#############
# EDIC      # 
#############

class EDIC(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.text
