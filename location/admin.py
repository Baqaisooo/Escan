from django.contrib import admin
from .models import Neighborhood

# Register your models here.


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    '''Admin View for Neighborhood'''

    list_display = ('city_id', 'neighborhood_name')
    list_filter = ('city_id',)

    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

