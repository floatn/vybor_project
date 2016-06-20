# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic

from .models import *
from contacts.models import Person
from images.models import Slides


class PersonListView(generic.ListView):
    model = Person
    template_name = "about/index_about.html"
    context_object_name = 'person_list'

    def get_context_data(self, **kwargs):
            context = super(PersonListView, self).get_context_data(**kwargs)
            context['slide_list'] = Slides.objects.all()
            context['nav_active_button'] = "About"
            return context


class AdvisorListView(PersonListView):
    model = Advisor

    def get_context_data(self, **kwargs):
            context = super(AdvisorListView, self).get_context_data(**kwargs)
            context['contact_title'] = 'Экспертный Совет'
            return context


class DirectionListView(PersonListView):
    model = Direction

    def get_context_data(self, **kwargs):
            context = super(DirectionListView, self).get_context_data(**kwargs)
            context['contact_title'] = 'Руководство'
            return context


class PartnerListView(generic.ListView):
    model = Partner
    template_name = 'about/partners_about.html'
    context_object_name = 'partner_list'

    def get_context_data(self, **kwargs):
            context = super(PartnerListView, self).get_context_data(**kwargs)
            context['slide_list'] = Slides.objects.all()
            context['nav_active_button'] = "About"
            return context
