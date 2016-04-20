from django.shortcuts import render
from django.views import generic

from .models import Partner
from images.models import Slides


class PartnerPageView(generic.ListView):
    model = Partners
    template_name = 'partners/index_partners.html'
    context_object_name = 'partners'

    def get_context_data(self, **kwargs):
            context = super(PartnersPageView, self).get_context_data(**kwargs)
            context['slide_list'] = Slides.objects.all()
            context['nav_active_button'] = "About"
            return context
