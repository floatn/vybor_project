from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    title_image = models.ImageField(upload_to='images/news/')
    title_image_small = models.ImageField(upload_to='images/news/small/')
    images = models.ManyToManyField("Image", blank=True, null=True)
    video = models.ManyToManyField("Video", blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Image(models.Model):
    image = models.ImageField(upload_to="images/")

    def __unicode__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __unicode__(self):
        return self.news_item.title+": "+self.image.name

class Video(models.Model):
    video = models.URLField()

    def __unicode__(self):
        return self.video.url

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'
