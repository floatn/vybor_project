from django.db import models

from contacts.models import Person

class Advisor(models.Model):
    person = models.OneToOneField(Person)

    def __unicode__(self):
        return self.person.last_name + ' ' + self.person.first_name
