from django.contrib import admin
# from .models import Species, Person
# Register your models here.
# admin.site.register(Species)
# admin.site.register(Person)

from django.apps import apps

all_models = apps.get_models()

for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

