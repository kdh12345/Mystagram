from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    list_filter = ['author']
    raw_id_fields = ['author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
