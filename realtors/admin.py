from django.contrib import admin

# Register your models here.

from .models import Realtor
# Registor your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_field = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
