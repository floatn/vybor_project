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
