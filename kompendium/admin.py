from django.contrib import admin

from kompendium.models import Topic, Subtopic, Entry, Kategorie, Link, US_Selektion, US_Bilderliste, News

# Register your models here.
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Entry)
admin.site.register(Kategorie)
admin.site.register(Link)
admin.site.register(US_Selektion)
admin.site.register(US_Bilderliste)
admin.site.register(News)
