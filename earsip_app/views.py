from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from . models import SemuaArsip, Disposisi, TempSuratKeluar, KlasifikasiSurat, ChecklistSubBag
from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime, date

# Create your views here.

@login_required(login_url="/accounts/login/")
def dashboard(request):



    context = {
        'page_title' : "Dashboard"
    }
    
    return render(request,'earsip/pages/dashboard.html' , context)


@login_required(login_url="/accounts/login/")
def tambah_surat(request):

    # now = datetime.today()
    # time_now = now.strftime("%Y-%m-%d")
    # # jam = now.strftime("%H:%M:%S")

    # print(time_now)

    # username = request.user
    # group_name = Group.objects.get(user = username)
    # print(group_name)
  
   
    
    klasifikasi_surat = list(KlasifikasiSurat.objects.all().values_list('klasifikasi', flat=True))


    tu = ['TataUsaha_SET','TataUsaha_ALPALHAN','TataUsaha_BMN','TataUsaha_POSKON','TataUsaha_PUSKOD']

   
    username = request.user
    group_name = Group.objects.get(user = username)
    group = str(group_name)

    print(group_name)
        
    if group in tu:
            is_tu = 1
    else:
            is_tu = 0
        
    print(is_tu)
        

    if request.method == 'POST':
            get_surat = request.POST.get('no_surat')
            get_kepada = request.POST.get('kepada')
            get_tanggal = request.POST.get('tanggal')
            get_perihal = request.POST.get('prihal')
            get_klasifikasi = request.POST.get('klasifikasi')
            get_file_name =  request.FILES.get('file_name')
            get_is_tu  = is_tu

                 
            temp_tambah_surat = TempSuratKeluar(

                    username          = username,
                    group             = group_name, 
                    no_surat          = get_surat,
                    kepada            = get_kepada,
                    tgl_surat         = get_tanggal,
                    perihal           = get_perihal,
                    klasifikasi       = get_klasifikasi,
                    upload_file_arsip = get_file_name,
                    is_tu             = get_is_tu

                )

            temp_tambah_surat.save()
            return redirect('surat_keluar')


    context = {
            'klasifikasi' : klasifikasi_surat
        }

    return render(request,'earsip/pages/surat/tambah_surat.html' , context)


def surat_keluar(request):


    try:
        username = request.user
        group_name = Group.objects.get(user = username)

        tempp_surat_keluar = TempSuratKeluar.objects.filter(group = group_name).values()
        # x = str(tempp_surat_keluar[0])
        # y = x.split('_')

        # temp_surat_final = y[0]

        # name_grup = 'TataUsaha'

        
        # if temp_surat_final == name_grup:
        #     is_admin = 1
        # else:
        #     is_admin = 0
        #     print("Ini Ga bener")

        # print(tempp_surat_keluar)


    except:
        pass

    

    context = {
        'temp_surat' : tempp_surat_keluar
    }

    return render(request,'earsip/pages/surat/surat_keluar.html', context)

























# @login_required(login_url="/accounts/login/")
# def laporan(request):
    
#     return render(request,'earsip/pages/laporan.html')



# ##### SURAT ###################################################################################

# @login_required(login_url="/accounts/login/")
# def surat(request):
#     username = request.user
#     group_name = Group.objects.get(user = username)

#     datasemuasurat = DatabaseSurat.objects.filter(group = group_name).values()


#     # x = instance.

#     context = { 
#         'datasemuasurat' : datasemuasurat
#     }
    
#     return render(request,'earsip/pages/surat/index.html' , context)



# def semua_surat(request):
#     username = request.user
#     group_name = Group.objects.get(user = username)

#     datasemuasurat = DatabaseSurat.objects.filter(group = group_name).values()

#     context = { 
#         'datasemuasurat' : datasemuasurat
#     }

#     return render(request,'earsip/pages/surat/semua_surat.html', context)


# @login_required(login_url="/accounts/login/")
# def surat_keluar(request):
#     username = request.user
#     group_name = Group.objects.get(user = username)

#     datasemuasurat = DatabaseSurat.objects.filter(group = group_name).values()

#     context = { 
#         'datasemuasurat' : datasemuasurat
#     }

#     return render(request,'earsip/pages/surat/surat_keluar.html', context)


# def duplikat_surat(request):

#     return render(request,'earsip/pages/surat/duplikat_surat.html')

# ### Setting Surat ###############################################################################

# def setting_klasifikasi(request):
#     username = request.user
#     group_name = Group.objects.get(user = username)

#     klasifikasi = KlasifikasiSurat.objects.filter(group = group_name).values()
#     subklasifikasi = SubKlasifikasiSurat.objects.filter(group = group_name).values()
    
#     context = { 
#         'klasifikasi'    : klasifikasi,
#         'subklasifikasi' : subklasifikasi
#     }

#     return render(request,'earsip/pages/surat/setting.html', context)


# def add_setting_klasifikasi(request):
     
#     if request.method == 'POST':
#         username = request.user
#         group_name = Group.objects.get(user = username)

#         klasifikasi = request.POST.get('klasifikasi_surat')
#         db_klasifikasi = KlasifikasiSurat(
#             group        = group_name,
#             username     = username,
#             klasifikasi  = klasifikasi
#         )

#         db_klasifikasi.save()

#         return redirect('setting_klasifikasi')
#     else:
#         return render(request,'pages/setting_klasifikasi.html')
    

# def edit_setting_klasifikasi(request, id_edit_klasifikasi):
#     edit_klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_edit_klasifikasi)
#     if request.method == 'POST':
#         username = request.user
#         group_name = Group.objects.get(user = username)

#         klasifikasi = request.POST.get('klasifikasi_surat')
    
#         edit_klasifikasi = KlasifikasiSurat(
#             id           = id_edit_klasifikasi, 
#             group        = str(group_name),
#             username     = str(username),
#             klasifikasi  = klasifikasi
#         )
#         edit_klasifikasi.save()

#         return redirect('setting_klasifikasi')
#     else:

#         return render(request,'earsip/pages/surat/setting.html')
    
# @login_required(login_url="/accounts/login/")
# def delete_setting_klasifikasi(request, id_delete_klasifikasi):
#     klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_delete_klasifikasi)

#     if request.method == 'POST':
#         klasifikasi.delete()
#         return redirect('setting_klasifikasi')
    


# def add_setting_subklasifikasi(request):
     
#     if request.method == 'POST':
#         username = request.user
#         group_name = Group.objects.get(user = username)

#         subklasifikasi = request.POST.get('subklasifikasi_surat')


#         db_subklasifikasi = SubKlasifikasiSurat(
#             group        = group_name,
#             username     = username,
#             subklasifikasi  = subklasifikasi,
#         )

#         db_subklasifikasi.save()
#         # db_klasifikasi.clean_fields()

#         return redirect('setting_klasifikasi')
#     else:
#         return render(request,'pages/setting_klasifikasi.html')
    
# def edit_setting_subklasifikasi(request, id_edit_setting_subklasifikasi):
#     edit_subklasifikasi = get_object_or_404(SubKlasifikasiSurat, pk = id_edit_setting_subklasifikasi)

#     if request.method == 'POST':
#         username = request.user
#         group_name = Group.objects.get(user = username)

#         subklasifikasi = request.POST.get('subklasifikasi_surat')
    
#         edit_subklasifikasi   = SubKlasifikasiSurat(

#             id                 = id_edit_setting_subklasifikasi, 
#             group              = str(group_name),
#             username           = str(username),
#             subklasifikasi     = subklasifikasi

#         )
#         edit_subklasifikasi.save()

#         return redirect('setting_klasifikasi')
#     else:

#         return render(request,'earsip/pages/surat/setting.html')
    

# @login_required(login_url="/accounts/login/")
# def delete_setting_subklasifikasi(request, id_delete_setting_subklasifikasi):
#     subklasifikasi = get_object_or_404(SubKlasifikasiSurat, pk = id_delete_setting_subklasifikasi)

#     if request.method == 'POST':
#         subklasifikasi.delete()
#         return redirect('setting_klasifikasi')

# def surat_terhapus(request):

#     return render(request,'earsip/pages/surat/surat_terhapus.html')




