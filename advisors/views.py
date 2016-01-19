from django.shortcuts import render
from django.views import generic
from .models import Advisor

from images.models import Slides


class AdvisorsPageView(generic.ListView):
    model = Advisor
    template_name = "advisors/index_advisors.html"
    context_object_name = "advisors"

    def get_context_data(self, **kwargs):
            context = super(AdvisorsPageView, self).get_context_data(**kwargs)
            context['slide_list'] = Slides.objects.all()
            context['nav_active_button'] = "About"
            return context
