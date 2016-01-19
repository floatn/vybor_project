from django.shortcuts import render
from django.views import generic

from .models import Video
from images.models import Slides


class VideoPageView(generic.ListView):
        model = Video
	template_name = 'video/index_video.html'
        context_object_name = 'video_list'

        def get_context_data(self, **kwargs):
                context = super(VideoPageView, self).get_context_data(**kwargs)
                context['slide_list'] = Slides.objects.all()
                context['nav_active_button'] = "Media"
                return context
