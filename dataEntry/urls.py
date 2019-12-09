
from django.urls import path
from dataEntry.views import dataEntryCase, homepage

app_name = "DataEntry"

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('/updateCaseData/<int:pk>/', dataEntryCase, name = 'DE_updateCase'),
    # path('ajax/delete_document', delete_document, name='ajax_delete_document'),
    # path('ajax/load-cities', load_cities, name='ajax_load_cities'),
    # path('ajax/load_neighborhoods', load_neighborhoods, name='ajax_load_neighborhoods'),
    # path('ajax/load_inspectors', load_inspectors, name='ajax_load_inspectors'),
    # path('/coordinatorUpdateCase/<int:pk>', coordinatorUpdateCase, name = 'coordinatorUpdateCase'),
    
] 
