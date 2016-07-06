# -*- coding: utf-8 -*-
from django.db import models

from contacts.models import Person
from strategy.models import Paragraph


class RelatedPerson(models.Model):
    related_person = models.ForeignKey('contacts.person')

    def __unicode__(self):
        return self.related_person.__unicode__()

    class Meta:
        verbose_name = 'Представитель'
        verbose_name_plural = 'Представители'


class Advisor(RelatedPerson):

    class Meta:
        verbose_name = 'Представитель экспертного совета'
        verbose_name_plural = 'Экспертный совет'


class Direction(RelatedPerson):

    class Meta:
        verbose_name = 'Представитель руководства'
        verbose_name_plural = 'Руководство'


class Strategy(Paragraph):

    class Meta:
        proxy = True
        verbose_name = 'Стратегия'
        verbose_name_plural = 'Стратегия'


class Partner(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()
    logo = models.ImageField(upload_to='images/logo/')
    link = models.URLField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
