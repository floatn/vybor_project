from django.shortcuts import render
from django.views import generic

from .models import Person, Office, Email, Phone
from images.models import Slides


class ContactsPageView(generic.ListView):
    model = Person
    template_name = 'contacts/index_contacts.html'
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super(ContactsPageView, self).get_context_data(**kwargs)
        context['slide_list'] = Slides.objects.all()
        context['office'] = Office.objects.all()
        context['nav_active_button'] = 'Contacts'
        return context
