from django.contrib import admin
from .models import internal_letter,external_letter,external_past,internal_past

admin.site.register(internal_letter)
admin.site.register(external_letter)
admin.site.register(external_past)
admin.site.register(internal_past)