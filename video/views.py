from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from images.models import Slides


class VideoPageView(generic.ListView):
        model = Video
	template_name = 'video/index_video.html'
        context_object_name = 'video_list'
        paginate_by = 9

        def get_context_data(self, **kwargs):
                context = super(VideoPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Media"
                paginator = Paginator(Video.objects.all(), self.paginate_by)
                page = self.request.GET.get('page')
                try:
                    file_video = paginator.page(page)
                except PageNotAnInteger:
                    file_video = paginator.page(1)
                except EmptyPage:
                    file_video = paginator.page(paginator.num_pages)
                context['video_page'] = file_video
                print(context.keys())
                return context
