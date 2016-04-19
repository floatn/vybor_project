from django.contrib import admin
from .models import *

# Register your models here.


class PersonPhoneAdminInline(admin.TabularInline):
    model = PersonPhone
    extra = 1

class PersonEmailAdminInline(admin.TabularInline):
    model = PersonEmail
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PersonPhoneAdminInline,
        PersonEmailAdminInline,
    ]
admin.site.register(Office)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonEmail)
admin.site.register(OfficeEmail)
admin.site.register(PersonPhone)
admin.site.register(OfficePhone)
admin.site.register(Photo)
