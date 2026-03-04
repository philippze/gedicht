from django.contrib import admin

from .models import Bestellung


class BestellungAdmin(admin.ModelAdmin):
    list_display = ['name', 'zeitpunkt']

admin.site.register(Bestellung, BestellungAdmin)
