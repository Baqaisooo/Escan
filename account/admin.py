from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import USERCreationForm
from .models import User, Region, City

# Register your models here.

class USERAdmin(UserAdmin):
    add_form = USERCreationForm
    model = User
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'region', 'city', 'date_joined', 'updated_at')
    personal_info = UserAdmin.fieldsets[1][1]['fields']+('phone', 'region', 'city',)
    fieldsets = ((UserAdmin.fieldsets[0]),)+(('Personal info', {'fields': personal_info}),)+UserAdmin.fieldsets[2:]

admin.site.register(User, USERAdmin)

admin.site.register(Region)
admin.site.register(City)