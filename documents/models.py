from django.db import models


class Documents(models.Model):
    file = models.FileField(upload_to="media/docs/")
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="media/icons", blank=True, null=True)

    def __unicode__(self):
        return self.file.name

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents" 
        
