from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from . models import DatabaseSurat, DeleteSurat, KlasifikasiSurat, SubKlasifikasiSurat
from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime, date

# Create your views here.

@login_required(login_url="/accounts/login/")
def dashboard(request):

    y = request.user

    x = Group.objects.get(user = y)

    print(y)
    print(x)

    context = {
        'page_title' : "Dashboard"
    }
    
    return render(request,'earsip/pages/dashboard.html' , context)


@login_required(login_url="/accounts/login/")
def laporan(request):
    
    return render(request,'earsip/pages/laporan.html')



##### SURAT ###################################################################################

@login_required(login_url="/accounts/login/")
def surat(request):



    
    return render(request,'earsip/pages/surat/index.html')


@login_required(login_url="/accounts/login/")
def surat_harian(request):


    

    return render(request,'earsip/pages/surat/surat_harian.html')


@login_required(login_url="/accounts/login/")
def tambah_surat(request):

    # id_username = request.user.pk
    # username = request.user

    # now = datetime.now()
    # year = now.strftime("%Y")

    # hari_ini = date.today()
    # klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    # kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   
    # get_surat = request.POST.get('surat')
    # get_klasifikasi = request.POST.get('klasifikasi')
    # get_kelompok = request.POST.get('kelompok')
    # get_tanggal = request.POST.get('tanggal')

    # files_upload = request.FILES.get('file_name')
    # files_name = str(files_upload).split(',')

    # filename_list_count = len(files_name)
   
    # try:  
    #     no_surat = files_name[0]
    #     kepada = files_name[1]
    #     prihal = files_name[2] 
    #     prihal_surat = prihal[:-4]

    #     upload_data = DatabaseSurat(
    #         id_user     = id_username,
    #         username    = username,
    #         surat       = get_surat,
    #         klasifikasi = get_klasifikasi,
    #         kelompok    = get_kelompok,
    #         tgl         = get_tanggal,
    #         no_surat    = no_surat,
    #         kepada      = kepada,
    #         perihal     = prihal_surat,
    #         upload_file = files_upload,
    #         today       = hari_ini,
    #         tahun       = year,
    #     )
        
    # except Exception:
    #     pass
        
    # else:
    #     if filename_list_count == 3:
    #         upload_data.save()
    #         return redirect('home')
    #     else:
    #         # messages.warning(request,'bzdbdbzdb')
    #         print("ada yang salah, cek lagi ")
        
    # context = {
    #     'page_title' : 'Tambah Data',
    #     'klasifikasi' : klasifikasi,
    #     'kelompok' : kelompok,
        
    # }
   

    return render(request,'earsip/pages/surat/tambah_surat.html')

def duplikat_surat(request):

    return render(request,'earsip/pages/surat/duplikat_surat.html')

### Setting Surat ###############################################################################

def setting_klasifikasi(request):
    username = request.user
    group_name = Group.objects.get(user = username)

    klasifikasi = KlasifikasiSurat.objects.filter(group = group_name).values()
    subklasifikasi = SubKlasifikasiSurat.objects.filter(group = group_name).values()
    
    context = { 
        'klasifikasi'    : klasifikasi,
        'subklasifikasi' : subklasifikasi
    }

    return render(request,'earsip/pages/surat/setting.html', context)


def add_setting_klasifikasi(request):
     
    if request.method == 'POST':
        username = request.user
        group_name = Group.objects.get(user = username)

        klasifikasi = request.POST.get('klasifikasi_surat')


        db_klasifikasi = KlasifikasiSurat(
            group        = group_name,
            username     = username,
            klasifikasi  = klasifikasi
        )

        db_klasifikasi.save()
        # db_klasifikasi.clean_fields()

        return redirect('setting_klasifikasi')
    else:
        return render(request,'pages/setting_klasifikasi.html')
    

def edit_setting_klasifikasi(request, id_edit_klasifikasi):
    edit_klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_edit_klasifikasi)
    if request.method == 'POST':
        username = request.user
        group_name = Group.objects.get(user = username)

        klasifikasi = request.POST.get('klasifikasi_surat')
    
        edit_klasifikasi = KlasifikasiSurat(
            id           = id_edit_klasifikasi, 
            group        = str(group_name),
            username     = str(username),
            klasifikasi  = klasifikasi
        )
        edit_klasifikasi.save()

        return redirect('setting_klasifikasi')
    else:

        return render(request,'earsip/pages/surat/setting.html')
    
@login_required(login_url="/accounts/login/")
def delete_setting_klasifikasi(request, id_delete_klasifikasi):
    klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_delete_klasifikasi)

    if request.method == 'POST':
        klasifikasi.delete()
        return redirect('setting_klasifikasi')
    


def add_setting_subklasifikasi(request):
     
    if request.method == 'POST':
        username = request.user
        group_name = Group.objects.get(user = username)

        subklasifikasi = request.POST.get('subklasifikasi_surat')


        db_subklasifikasi = SubKlasifikasiSurat(
            group        = group_name,
            username     = username,
            subklasifikasi  = subklasifikasi,
        )

        db_subklasifikasi.save()
        # db_klasifikasi.clean_fields()

        return redirect('setting_klasifikasi')
    else:
        return render(request,'pages/setting_klasifikasi.html')
    
    

def surat_terhapus(request):

    return render(request,'earsip/pages/surat/surat_terhapus.html')





def semua_surat(request):
    return render(request,'earsip/pages/surat/semua_surat.html')