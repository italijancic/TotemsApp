from django.contrib import admin
from .models import Totem

# Register your models here.
class TotemAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'label', 'location')

admin.site.register(Totem, TotemAdmin)