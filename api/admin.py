from django.contrib import admin
from .models import Customer,Contact
# Register your models here.

all_models=(Contact, Customer)
admin.site.register(all_models)