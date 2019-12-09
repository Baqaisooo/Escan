from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages


def direct_to(role):
    role = role.lower()
    to = ''
    if role == 'المنسقين':
        to= "Coordinator:homepage"
    elif role == 'المدخلين':
        to = "DataEntry:homepage"
    elif role == 'المقيّمين':
        to = "Evaluator:homepage"

    return to

def login(request):
    if request.user.is_authenticated:
            role = request.user.groups.all().first().name
            to = direct_to(role)
            return redirect(to) if to else redirect('/')

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = email, password = password)

        if user:
            role = user.groups.all()[0].name.lower()
            to = direct_to(role)
            
            if to:
                auth.login(request, user)
                return redirect(to)
            else:
                return redirect('/')
        else:
            messages.info(request, 'الرجاء التأكد من اسم المستخدم و كلمة المرور')
            return redirect("Account:login")
    else:
        return render(request,'account/login.html',{})


def logout(request):
    auth.logout(request)
    return redirect("Account:login")