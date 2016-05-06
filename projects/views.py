from django.shortcuts import render
from django.views import generic

from .models import Project
from images.models import Slides


class ProjectsPageView(generic.ListView):
        model = Project
	template_name = 'projects/index_projects.html'
        context_object_name = 'projects'
	def get_context_data(self, **kwargs):
		context = super(ProjectsPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Projects"
		return context

class ProjectDetailsPageView(generic.DetailView):
        model = Project
	template_name = 'projects/details_projects.html'
        context_object_name = 'project'
	def get_context_data(self, **kwargs):
		context = super(ProjectDetailsPageView, self).get_context_data(**kwargs)
                sections = context['project'].description.split('[!img]')
                images = context['project'].images.all()
                sec_len, img_len = len(sections), len(images)
                min_len = min(sec_len-1, img_len)
                sections = sections[:min_len] + [''.join(sections[min_len:sec_len])]
                images = images[:min_len] + [None]
                context['zip'] = zip(sections, images)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Projects"
                #print(context['zip'])
		return context
