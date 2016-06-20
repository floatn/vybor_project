from django.contrib import admin

from .models import Project


'''
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('images', 'image_thumb',),
            'readonly_fields': ('images', 'image_thumb',),},),)
    readonly_fields = ['image_thumb',]
'''

admin.site.register(Project)#, ProjectAdmin)
