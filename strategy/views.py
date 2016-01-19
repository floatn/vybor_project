from django.shortcuts import render
from django.views import generic

from .models import Paragraph
from images.models import Slides


class StrategyPageView(generic.ListView):
        model = Paragraph
	template_name = 'strategy/index_strategy.html'
        context_object_name = 'paragraphs'

        def get_context_data(self, **kwargs):
                context = super(StrategyPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "About"
                return context
