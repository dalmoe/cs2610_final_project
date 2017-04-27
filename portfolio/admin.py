from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_name']}),
        ('Description', {'fields': ['project_description']}),
        ('Source links', {'fields': ['project_source']}),
        ]
admin.site.register(Project, ProjectAdmin)