from django.shortcuts import render
from django.views import generic
from news.models import News


class HomePageView(generic.ListView):
	template_name = 'home/index_home.html'
        context_object_name = 'latest_news_list'

        def get_queryset(self):
            queryset = News.objects.all()[:5]
            for i in queryset:
                i.description = i.description[:95] + '...'
            return queryset
        
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
                context['nav_active_button'] = "Home"
		return context
