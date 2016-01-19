from django.shortcuts import render
from django.views import generic

from .models import Image, Slides


class ImagePageView(generic.ListView):
        model = Image
	template_name = 'images/index_images.html'
        context_object_name = 'images_list'

        def get_context_data(self, **kwargs):
                context = super(ImagePageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Media"
                return context
