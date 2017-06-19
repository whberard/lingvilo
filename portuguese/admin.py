from django.contrib import admin
from .models import Verb, Reason, End, Start

class StartAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'translation','why')
    filter_horizontal = ('ends',)


admin.site.register(Verb)
admin.site.register(Reason)
admin.site.register(End)
admin.site.register(Start, StartAdmin)
