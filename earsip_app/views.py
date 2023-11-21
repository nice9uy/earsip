from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

@login_required(login_url="/accounts/login/")
def dashboard(request):

    x = Group.objects.get()

    print(x)

    context = {
        'page_title' : "Dashboard"
    }
    
    return render(request,'earsip/pages/dashboard.html' , context)


@login_required(login_url="/accounts/login/")
def laporan(request):
    
    return render(request,'earsip/pages/laporan.html')


@login_required(login_url="/accounts/login/")
def surat(request):



    
    return render(request,'earsip/pages/laporan.html')


@login_required(login_url="/accounts/login/")
def tambah_surat(request):



    return render(request,'earsip/pages/surat/tambah_surat.html')


def semua_surat(request):
    return render(request,'earsip/pages/surat/semua_surat.html')