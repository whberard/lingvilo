from django.contrib import admin
from .models import Verb, Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation', 'is_known', 'last_review')
    ordering = ('word',)
    date_hierarchy = 'last_review'

admin.site.register(Word, WordAdmin)

