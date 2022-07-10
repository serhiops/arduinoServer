from django.contrib import admin
from .models import Clicks


class ClicksAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip','created', 'updated')
    list_display_links = ('id', 'ip')



admin.site.register(Clicks, ClicksAdmin)

