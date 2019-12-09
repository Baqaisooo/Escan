from django.contrib import admin
from .models        import Status, RealEstate, Case, UserCase, RealEstateDocument, CaseStatus

# Register your models here.

class RealEstateDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'document', 'realEstate')

admin.site.register(RealEstateDocument, RealEstateDocumentAdmin)


class UserCaseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'case_id', 'create_at')

admin.site.register(UserCase, UserCaseAdmin)



class CaseAdmin(admin.ModelAdmin):
    list_display = ('pk','realEstate', 'created_at')
    ordering = ('pk',)
admin.site.register(Case, CaseAdmin)


class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('pk','contact_name', 'contact_number', 'region_id', 'city_id', 'neighborhood_id', 'location', 'coordinator_note')
    ordering = ('pk',)
admin.site.register(RealEstate, RealEstateAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk','id','status_for', 'status')
    ordering = ('pk',)
admin.site.register(Status, StatusAdmin)


@admin.register(CaseStatus)
class CaseStatusAdmin(admin.ModelAdmin):
    '''Admin View for CaseStatus'''

    list_display = ('pk', 'case', 'status', 'isActive', 'InspectorUpdate', 'dataEntryUpdate', 'create_at')
    ordering = ('pk',)