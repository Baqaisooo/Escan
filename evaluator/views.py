from django.shortcuts   import render, redirect, get_object_or_404
from django.http        import HttpResponse, HttpResponseRedirect
from django.urls        import reverse
# from .forms             import DataEntryForm
from account.views      import direct_to
from django.contrib     import messages

from django.contrib.auth.models import Group
from case.models        import Case, Status, UserCase, RealEstateDocument, RealEstate, CaseStatus
from datetime           import datetime


# Create your views here.



def homepage(request):
    if request.user.is_authenticated:
        role = request.user.groups.all().first().name

        if(role == 'المقيّمين'):
            # try:
            #     status = Status.objects.get(pk=1)
            # except Status.DoesNotExist:
            #     raise
            context = {#############################33
                'inspected_cases'     : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=7), Status.objects.get(pk=14)], isActive=True ),
                'evaluated_cases'     : CaseStatus.objects.filter(status = Status.objects.get(pk=15), isActive=True ),
            }
            return render(request, 'evaluator/homepage.html', context)  
        else: redirect('Account:login')
    else: return redirect('Account:login')


