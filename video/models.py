from django.db import models


class Video(models.Model):
    link = models.URLField()
    img_link = models.URLField(default="http://img.youtube.com/vi//0.jpg")
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return (self.description[:50] or link)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"
