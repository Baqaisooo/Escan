
from django.urls import path
from coordinator.views import *

app_name = "Coordinator"

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('/new_case', createNewCase, name = 'new_case'),
    path('ajax/delete_document', delete_document, name='ajax_delete_document'),
    path('ajax/load-cities', load_cities, name='ajax_load_cities'),
    path('ajax/load_neighborhoods', load_neighborhoods, name='ajax_load_neighborhoods'),
    path('ajax/load_inspectors', load_inspectors, name='ajax_load_inspectors'),
    path('/coordinatorUpdateCase/<int:pk>', coordinatorUpdateCase, name = 'coordinatorUpdateCase'),
    
] 
