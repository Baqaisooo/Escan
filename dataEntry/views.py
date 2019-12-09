from django.shortcuts   import render, redirect, get_object_or_404
from django.http        import HttpResponse, HttpResponseRedirect
from django.urls        import reverse
from .forms             import DataEntryForm
from account.views      import direct_to
from django.contrib     import messages

from django.contrib.auth.models import Group
from case.models        import Case, Status, UserCase, RealEstateDocument, RealEstate, CaseStatus
from datetime           import datetime


# Create your views here.



def homepage(request):
    if request.user.is_authenticated:
        role = request.user.groups.all().first().name

        if(role == 'المدخلين'):
            # try:
            #     status = Status.objects.get(pk=1)
            # except Status.DoesNotExist:
            #     raise
            context = {#############################33
                'sent_cases'        : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=1), Status.objects.get(pk=2), Status.objects.get(pk=3), Status.objects.get(pk=4), Status.objects.get(pk=5), Status.objects.get(pk=6), Status.objects.get(pk=7)], isActive=True ),
                'entered_cases'  : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=8), Status.objects.get(pk=9), Status.objects.get(pk=10), Status.objects.get(pk=11), Status.objects.get(pk=12), Status.objects.get(pk=13), Status.objects.get(pk=14)], isActive=True ),

                
            }
            return render(request, 'dataEntry/homepage.html', context)  
        else: redirect('Account:login')
    else: return redirect('Account:login')



def dataEntryCase(request, pk=None):
    instance = get_object_or_404(RealEstate, pk = pk)
    form = DataEntryForm(request.POST or None, instance= instance )

    if form.is_valid():
        realEstate = form.save()
        UserCase(user_id=request.user, case_id=realEstate.case).save()
        case = realEstate.case
        last_case_status = case.casestatus_set.last()
        pk = last_case_status.status.pk
        if pk <= 7:
            last_case_status.isActive = False
            last_case_status.save()
            case.casestatus_set.create(case = case, status = Status.objects.get( pk = (pk + 7) ), dataEntryUpdate=datetime.now() , InspectorUpdate=last_case_status.InspectorUpdate)
        else:
            last_case_status.isActive = False
            last_case_status.save()

            case.casestatus_set.create(case = case, status = Status.objects.get( pk = pk ), dataEntryUpdate=datetime.now() , InspectorUpdate=last_case_status.InspectorUpdate)

        messages.success(request, 'تم إدخال و تعديل البيانات بنجاح')
            
        return redirect('DataEntry:homepage')
        
    context = {
        'form'      : form,
        'case_ID'   : instance.pk,
        'files'     : instance.realestatedocument_set.all()
    }
    return render(request, 'dataEntry/updateCase.html', context)

