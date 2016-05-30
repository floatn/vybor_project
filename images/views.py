from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


class ImagePageView(generic.ListView):
        model = Image
	template_name = 'images/index_images.html'
        context_object_name = 'images_list'
        paginate_by = 15

        def get_context_data(self, **kwargs):
                context = super(ImagePageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Media"
                paginator = Paginator(Image.objects.all(), self.paginate_by)
                page = self.request.GET.get('page')
                try:
                    file_images = paginator.page(page)
                except PageNotAnInteger:
                    file_images = paginator.page(1)
                except EmptyPage:
                    file_images = paginator.page(paginator.num_pages)
                context['image_page'] = file_images
                print(context.keys())
                return context
