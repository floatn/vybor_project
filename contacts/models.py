from django.db import models
#import phonenumbers


class Office(models.Model):
    address = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.address


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_photo = models.OneToOneField('Photo', blank=True, null=True)

    def __unicode__(self):
        return ' '.join([self.last_name, self.first_name, self.father_name])


class Email(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email

 
class PersonEmail(Email):
    owner_person = models.ForeignKey('Person', blank=True, null=True)

 
class OfficeEmail(Email):
    owner_office = models.ForeignKey('Office', blank=True, null=True)

 
class Phone(models.Model):
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        parsed_number = self.phone#phonenumbers.parse(self.phone, 'RU')
        formatted_number = self.phone#phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return formatted_number


class PersonPhone(Phone):
    owner_person = models.ForeignKey('Person', blank=True, null=True)


class OfficePhone(Phone):
    owner_office = models.ForeignKey('Office', blank=True, null=True)


class Photo(models.Model):
    image = models.ImageField(upload_to='images/photo/')
    owner_person = models.ForeignKey('Person', blank=True, null=True)

    def __unicode__(self):
        return self.image.name
