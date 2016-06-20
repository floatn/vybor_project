from django.db import models

from video.models import Video
from images.models import Image

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    title_image = models.ImageField(upload_to='images/news/', blank=True)
    images = models.ManyToManyField(Image, blank=True)
    #title_image_small = models.ImageField(upload_to='images/news/small/')
    video = models.ManyToManyField(Video, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
