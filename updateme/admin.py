from django.contrib import admin
from .models import NeighbourHood, User, Business, Admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(NeighbourHood)
admin.site.register(Business)