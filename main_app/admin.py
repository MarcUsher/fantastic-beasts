from django.contrib import admin
from .models import Beast, Walk, Location

# Register your models here.
admin.site.register(Beast)
admin.site.register(Walk)
admin.site.register(Location)