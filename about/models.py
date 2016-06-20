from django.db import models

from contacts.models import Person
from strategy.models import Paragraph


class RelatedPerson(models.Model):
    related_person = models.ForeignKey('contacts.person')

    def __unicode__(self):
        return self.related_person.__unicode__()


class Advisor(RelatedPerson): pass


class Direction(RelatedPerson):

    class Meta:
        verbose_name_plural = 'Direction'


class Strategy(Paragraph):

    class Meta:
        proxy = True
        verbose_name_plural = 'Strategy'


class Partner(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    logo = models.ImageField(upload_to='images/logo/')
    link = models.URLField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
