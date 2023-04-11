from django.contrib import admin
from .models import ContactsModel, UserProfile

# Register your models here.
admin.site.register(ContactsModel)
admin.site.register(UserProfile)
