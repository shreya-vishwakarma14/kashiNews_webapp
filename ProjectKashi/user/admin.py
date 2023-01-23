from django.contrib import admin

# Register your models here.
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Email', 'Number', 'DOB', 'Password', 'ConfirmPassword')


admin.site.register(Contact, ContactAdmin)
