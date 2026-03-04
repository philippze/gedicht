from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import BestellungForm
from .models import Bestellung


class KeinValentinstagsgedichtView(TemplateView):
    template_name = "kein-valentinstagsgedicht.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BestellungForm(initial={'name': 'Valentinstagsgedicht'})
        return context


class BestellungCreateView(CreateView):
    model = Bestellung
    form_class = BestellungForm

    def get(self, *args, **kwargs):
        raise Http404

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Gedicht bestellt',
            message='bitte eines schreiben...',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['philipp@zedler.it']
        )
        return HttpResponse("""
        <p style="margin-top: 40px;">
            Danke für die Bestellung. Ich denk mir was aus und melde mich dann.
        </p>
        <p>
            Hoffentlich hat mit der Technik alles geklappt...
        </p>
        """)