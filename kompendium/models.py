from __future__ import unicode_literals

from django.db import models

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

#############
# FORM TEST #
#############

class Rechner(models.Model):
    natrium = models.IntegerField()
    kalium = models.IntegerField()

    def __unicode__(self):
        return (self.natrium, self.kalium) 
