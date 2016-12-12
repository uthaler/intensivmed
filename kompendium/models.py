from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.text[:50] + "..."

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
