from atexit import register
from django.contrib import admin

from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['address','email','phone','created_on']

