from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.views.generic import View

from Housing.utils import get_pdf
import datetime

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.datetime.now(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('case/pdfCase.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

def print_to_pdf(request):
    data = dict()
    return get_pdf('case/pdfCase.html', { 'data': data })

# def genericPDF(request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')