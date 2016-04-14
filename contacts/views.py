from django.shortcuts import render
from django.views import generic

from .models import Person, Office#, Email, Phone
from images.models import Slides


class ContactListView(generic.ListView):
    model = Person
    template_name = 'contacts/index_contacts.html'
    context_object_name = 'contact_list'

    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        context['slide_list'] = Slides.objects.all()
        context['office_list'] = Office.objects.all()
        context['nav_active_button'] = 'Contacts'
        return context
