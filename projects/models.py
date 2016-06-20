from django.db import models

from news.models import News
from images.models import Image
from video.models import Video


class Project(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    date_started = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    appointments = models.ManyToManyField(News, blank=True)
    title_image = models.ForeignKey(Image, related_name='title_image', blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)
    video = models.ManyToManyField(Video, blank=True)

    '''
    def image_tag(self):
        return u'<img src="%s" />' % self.images.url

    image_tag.short_description = 'Image'
    def image_thumb(self):
        return '<img src="/media/%s" width="20" height="20" /> % (self.images.object.0)'
    image_thumb.allow_tags = True
    '''

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ('-date_started',)
