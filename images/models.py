from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.TextField(blank=True, null=True)
    group = models.ForeignKey('ImageGroup', blank=False, null=True)

    def __unicode__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

class Slides(models.Model):
    image = models.ImageField(upload_to="images/slides/")
    caption = models.TextField(blank=True, null=True)

    class Meta:
            verbose_name = 'Slide'
            verbose_name_plural = 'Slides'

class ImageGroup(models.Model):
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
