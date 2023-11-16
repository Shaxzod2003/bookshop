from django.contrib import admin
from .models import Customer,Contact, Publisher, Language,Book,Author,Genre
# Register your models here.

all_models=(Contact, Customer,Publisher,Language,Book,Author,Genre)
admin.site.register(all_models)