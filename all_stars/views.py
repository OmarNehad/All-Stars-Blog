from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutPage(TemplateView):
    template_name='about.html'

class ContactPage(TemplateView):
    template_name ='contact.html'
