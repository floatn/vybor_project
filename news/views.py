from django.shortcuts import render

from django.views import generic
from .models import News


class NewsPageView(generic.ListView):
	template_name = 'news/index.html'
        context_object_name = 'latest_news_list'
        queryset = News.objects.all()
