from django.db import models

from contacts.models import Person

class Advisor(models.Model):
    person = models.OneToOneField(Person)
    template_name = "advisors/index_advisors.html"
    context_object_name = "advisors"

    def __unicode__(self):
        return self.person.last_name + ' ' + self.person.first_name
