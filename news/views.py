from django.shortcuts import render

from django.views import generic
from .models import News
from images.models import Slides


class NewsPageView(generic.ListView):
	template_name = 'news/index_news.html'
        context_object_name = 'latest_news_list'
        queryset = News.objects.all()
	def get_context_data(self, **kwargs):
		context = super(NewsPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                #context['nav_active_button'] = "Projects"
                #print(context['zip'])
		return context
