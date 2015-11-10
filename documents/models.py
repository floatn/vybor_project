from django.db import models


class Documents(models.Model):
    file = models.FileField(upload_to="docs/")
    description = models.CharField(max_length=255)
