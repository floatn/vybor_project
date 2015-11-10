from django.shortcuts import render
from django.views import generic

from .models import Documents


class DocumentsPageView(generic.ListView):
        model = Documents
	template_name = 'documents/index_documents.html'
        context_object_name = "document_list"
	def get_context_data(self, **kwargs):
		context = super(DocumentsPageView, self).get_context_data(**kwargs)
		context['nav_active_button'] = 'Documents'
		return context
