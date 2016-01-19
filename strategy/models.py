from django.db import models

from video.models import Video
from images.models import Image

class Paragraph(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Image, blank=True, null=True)
    video = models.ManyToManyField(Video, blank=True, null=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Strategy"
        verbose_name_plural = "Strategy"
