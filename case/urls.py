
from django.urls import path
from case.views import print_to_pdf

app_name = "Case"

urlpatterns = [
    path('', print_to_pdf, name = 'GeneratePdf')
    
] 
