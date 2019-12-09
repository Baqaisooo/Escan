from django.shortcuts   import render, redirect, get_object_or_404
from django.http        import HttpResponse, HttpResponseRedirect
from django.urls        import reverse
from .forms             import CaseForm
from account.views      import direct_to
from django.contrib     import messages

from django.contrib.auth.models import Group
from case.models        import Case, Status, UserCase, RealEstateDocument, RealEstate, CaseStatus
from location.models    import City, Neighborhood
from datetime           import datetime

# Create your views here.

DOCUMENTS_TYPE = {
    '1':'صك',
    '2':'رخصة',
    '3':'كروكي',
    '4':'أخرى'
}


def homepage(request):
    if request.user.is_authenticated:
        role = request.user.groups.all().first().name

        if(role == 'المنسقين'):
            # try:
            #     status = Status.objects.get(pk=1)
            # except Status.DoesNotExist:
            #     raise
            context = {
                'sent_cases'        : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=1), Status.objects.get(pk=7)], isActive=True ),
                'apologized_cases'  : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=2), Status.objects.get(pk=8)], isActive=True ),
                'held_cases'        : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=3), Status.objects.get(pk=9)], isActive=True ),

                'waiting_time_cases': CaseStatus.objects.filter(status__in = [Status.objects.get(pk=4), Status.objects.get(pk=10)], isActive=True ),
                'waiting_inspect_cases': CaseStatus.objects.filter(status__in = [Status.objects.get(pk=5), Status.objects.get(pk=11)], isActive=True ),
                'delay_cases'       : CaseStatus.objects.filter(status__in = [Status.objects.get(pk=6), Status.objects.get(pk=12)], isActive=True )
            }
            return render(request, 'coordinator/homepage.html', context)  
        else: redirect('Account:login')
    else: return redirect('Account:login')



def createNewCase(request):
    form = CaseForm(request.POST or None)

    if form.is_valid():
        docs_type   = request.POST.getlist('file-type')
        docs        = request.FILES.getlist('docs')

        newRealEstate = form.save()
        newCase = Case(realEstate = newRealEstate)
        newCase.save()
        
        newCase.casestatus_set.create(case = newCase, status = Status.objects.get( pk = 1 ), dataEntryUpdate=datetime.now() , InspectorUpdate=datetime.now())

        # newCase.status.add(Status.objects.get(pk=1))
        UserCase(user_id=request.user, case_id=newCase).save()        
        UserCase(user_id=form.cleaned_data['inspector'], case_id=newCase).save()  

        if docs and docs_type:
            for (doc, doc_type) in zip(docs, docs_type):
                newRealEstate.realestatedocument_set.create(document=doc, document_type=DOCUMENTS_TYPE[doc_type])


        messages.success(request, 'تمت إضافة المعاملة بنجاح وإرسالها للمعاين {}'.format(form.cleaned_data['inspector']))
        form = CaseForm()
        return HttpResponseRedirect(reverse('Coordinator:new_case'))
    
    context = {
        'form' : form,
    }
    return render(request, 'coordinator/createNewCase.html', context)



def coordinatorUpdateCase(request, pk):
    # instance = get_object_or_404(MyModel, id=id)
    # form = MyForm(request.POST or None, instance=instance)
    # return render(request, 'my_template.html', {'form': form}) 

    # if request.method == 'GET':
    instance = get_object_or_404(Case, pk=pk)
    form = CaseForm(request.POST or None, instance=instance.realEstate)

    CaseUser = instance.user.all()
    g = Group.objects.get(name = 'المعاينين').user_set.all()
    selected_inspector = CaseUser.intersection(g).last()
    
    if form.is_valid():
        updateRealEstate = form.save()

        newInspector = False
        if selected_inspector != form.cleaned_data['inspector']:

            case_inspector = UserCase.objects.get(case_id=instance, user_id = selected_inspector)
            case_inspector.user_id = form.cleaned_data['inspector']
            case_inspector.save()

            newInspector = True
        
        docs_type   = request.POST.getlist('file-type')
        docs        = request.FILES.getlist('docs')

        if docs and docs_type:
            for (doc, doc_type) in zip(docs, docs_type):
                updateRealEstate.realestatedocument_set.create(document=doc, document_type=DOCUMENTS_TYPE[doc_type])

        if newInspector:
            messages.success(request, 'تم تغيير المعاين بنجاح وإرسال المعاملة له')
        messages.success(request, 'تم تعديل البيانات بنجاح')
            
        return redirect('Coordinator:homepage')
    
    context = {
        'is_update'         : True,
        'selected_inspector': selected_inspector,
        'form'              : form,
        'case_ID'           : instance.pk,
        'files'             : instance.realEstate.realestatedocument_set.all()
    }

    return render(request, 'coordinator/createNewCase.html', context)
        


def delete_document(request):
    pk = request.GET.get('pk')
    if pk:
        document = get_object_or_404(RealEstateDocument, pk=pk)
        document.delete()
        return HttpResponse('done')
    return HttpResponse('error')



def load_cities(request):
    region = request.GET.get('region')
    cities = City.objects.filter(region = region).order_by('city')
    return render(request, 'coordinator/city_dropdown_list_options.html', {'cities': cities})


def load_neighborhoods(request):
    city = request.GET.get('city')
    neighborhoods = Neighborhood.objects.filter(city_id = city).order_by('neighborhood_name')
    return render(request, 'coordinator/neighborhood_dropdown_list_options.html', {'neighborhoods': neighborhoods})


def load_inspectors(request):
    city = request.GET.get('city')
    inspectors = Group.objects.filter(name = 'المعاينين').first().user_set.filter(city = city)
    return render(request, 'coordinator/inspector_dropdown_list_options.html', {'inspectors': inspectors})