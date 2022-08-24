from django.contrib import admin
from .models import Project, Technologie

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display = ('name',)
    search_fields = ('name', 'id')

class TechnologieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display = ('name',)
    search_fields = ('name', 'id')



admin.site.register(Project,ProjectAdmin)
admin.site.register(Technologie, TechnologieAdmin)