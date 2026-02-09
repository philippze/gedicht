from django.shortcuts import render
from django.views.generic.base import TemplateView



class KeinValentinstagsgedichtView(TemplateView):
    template_name = "kein-valentinstagsgedicht.html"
