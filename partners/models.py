from django.db import models

from images.models import Image


class Partners(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    image = models.ForeignKey(Image, blank=True, null=True)
    link = models.URLField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
