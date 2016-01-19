from django.shortcuts import render
from django.views import generic

from .models import Documents
from images.models import Slides


class DocumentsPageView(generic.ListView):
        model = Documents
	template_name = 'documents/index_documents.html'
        context_object_name = "document_list"
	def get_context_data(self, **kwargs):
		context = super(DocumentsPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
		context['nav_active_button'] = 'Documents'
		return context
