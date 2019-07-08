from django.contrib import admin

from .models import NoteModel

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at')


admin.site.register(NoteModel, NoteAdmin)
