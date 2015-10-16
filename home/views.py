from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
	template_name = 'templates/home.html'
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['latest_articles'] = 'Okaerinasai!'
		return context
