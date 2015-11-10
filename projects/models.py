from django.db import models

from news.models import News, Image, Video

class Project(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    date_started = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    appointments = models.ManyToManyField(News, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True, null=True)
    video = models.ManyToManyField(Video, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
