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
                new_object_list = []
                for object in context['document_list']:
                    created_time = object.file.storage.created_time(object.file.name)
                    new_object_list.append((object, created_time))
                context['document_list'] = new_object_list
                context['slide_list'] = Slides.objects.all()
		context['nav_active_button'] = 'Documents'
		return context
