from django.shortcuts import render
from django.views import generic

from .models import Project


class ProjectsPageView(generic.ListView):
        model = Project
	template_name = 'projects/index_projects.html'
        context_object_name = 'projects'
	def get_context_data(self, **kwargs):
		context = super(ProjectsPageView, self).get_context_data(**kwargs)
                context['nav_active_button'] = "Projects"
		return context
