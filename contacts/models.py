from django.db import models


class Office(models.Model):
    address = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.address

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    main_photo = models.OneToOneField('Photo', blank=True, null=True)

    def __unicode__(self):
        return ' '.join([self.last_name, self.first_name, self.father_name])

class Email(models.Model):
    email = models.EmailField()
    owner_person = models.ForeignKey('Person', blank=True, null=True)

    def __unicode__(self):
        return self.email

class Phone(models.Model):
    phone = models.CharField(max_length=20)
    owner_person = models.ForeignKey('Person', blank=True, null=True)
    owner_office = models.ForeignKey('Office', blank=True, null=True)

    def __unicode__(self):
        return self.phone

class Photo(models.Model):
    image = models.ImageField(upload_to="photo")
    owner_person = models.ForeignKey('Person')

    def __unicode__(self):
        return self.image.name
