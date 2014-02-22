from django.contrib import admin
from rsvp.models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'attendance')

admin.site.register(Guest, GuestAdmin)
