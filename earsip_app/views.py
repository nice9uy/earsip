from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from . models import SemuaArsip, Disposisi, KlasifikasiSurat, ChecklistSubBag
from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime, date

# Create your views here.

@login_required(login_url="/accounts/login/")
def dashboard(request):

    username = request.user
    group_name = Group.objects.get(user = username)


    # tempp_surat_keluar = TempSuratKeluar.objects.filter(group = group_name , id = 4 ).values()

    # print(tempp_surat_keluar)

    # x = tempp_surat_keluar.filter('kepada')

    # print(x)
    

    context = {
        'page_title' : "Dashboard"
    }
    
    return render(request,'earsip/pages/dashboard.html' , context)


@login_required(login_url="/accounts/login/")
def tambah_surat(request):

    now = datetime.today()
    time_now = now.strftime("%Y-%m-%d")
    # # jam = now.strftime("%H:%M:%S")

    # print(time_now)

    # username = request.user
    # group_name = Group.objects.get(user = username)
    # print(group_name)
    
    try:
        tu = ['TataUsaha_SET','TataUsaha_ALPALHAN','TataUsaha_BMN','TataUsaha_POSKON','TataUsaha_PUSKOD']
        spri = ['Spri_SET','Spri_ALPALHAN','Spri_BMN','Spri_POSKON','Spri_PUSKOD']
        klasifikasi_surat = list(KlasifikasiSurat.objects.all().values_list('klasifikasi', flat=True))

        username = request.user
        group_name = Group.objects.get(user = username)
        group = str(group_name)
            
        if group in tu:
                is_tu = 1
        else:
                is_tu = 0

        if group in spri:
             is_spri = 1
        else:
             is_spri = 0
            
        # print(is_tu)
            
        if request.method == 'POST':
            get_surat = request.POST.get('no_surat')
            get_kepada = request.POST.get('kepada')
            get_tanggal = request.POST.get('tanggal')
            get_perihal = request.POST.get('prihal')
            get_klasifikasi = request.POST.get('klasifikasi')
            get_tanggal_dibuat = time_now
            get_file_name =  request.FILES.get('file_name')
            # get_is_read = 
            get_is_tu  = is_tu
            get_is_spri = is_spri

                 
            temp_tambah_surat = SemuaArsip(

                    username          = username,
                    group             = group_name, 

                    no_surat          = get_surat,
                    kepada            = get_kepada,
                    tgl_surat         = get_tanggal,
                    perihal           = get_perihal,
                    klasifikasi       = get_klasifikasi,
                    tanggal_dibuat    = get_tanggal_dibuat,
                    upload_file_arsip = get_file_name,
                    is_tu             = get_is_tu,
                    is_spri           = get_is_spri

                )

            temp_tambah_surat.save()
            return redirect('surat_keluar')
        
    except:
        pass

    context = {
                'klasifikasi' : klasifikasi_surat
            }

    return render(request,'earsip/pages/surat/tambah_surat.html' , context)


def surat_keluar(request):
    try:
        username = request.user
        group_name = Group.objects.get(user = username)

        tempp_surat_keluar = SemuaArsip.objects.filter(group = group_name).values()
        klasifikasi_surat = list(KlasifikasiSurat.objects.all().values_list('klasifikasi', flat=True))
    
    except:
        pass


    context = {
        'temp_surat' : tempp_surat_keluar,
        'klasifikasi': klasifikasi_surat
    }

    return render(request,'earsip/pages/surat/surat_keluar.html', context)



def edit_surat_keluar(request ,id_edit_surat_keluar):
    edit_surat = get_object_or_404(SemuaArsip, pk = id_edit_surat_keluar)

    if request.method == 'POST':

        username = request.user
        group_name = str(Group.objects.get(user = username))


        get_surat       = request.POST.get('no_surat')
        get_kepada      =  request.POST.get('kepada')
        get_tanggal     = request.POST.get('tanggal')
        get_perihal     = request.POST.get('prihal')
        get_klasifikasi = request.POST.get('klasifikasi')
        get_file_name   = edit_surat.upload_file_arsip.name
        get_is_tu       = edit_surat.is_tu
        
        
        edit_surat = SemuaArsip(
             
            id                 = id_edit_surat_keluar,
            username           = str(username), 
            group              = group_name,
            no_surat           = get_surat, 
            kepada             = get_kepada,
            tgl_surat          = get_tanggal,
            perihal            = get_perihal, 
            klasifikasi        = get_klasifikasi,
            upload_file_arsip  = get_file_name, 
            is_tu              = get_is_tu,
        )

        edit_surat.save()

        return redirect('surat_keluar')    
    
    context = {
            
    }

    return render(request,'earsip/pages/surat/surat_keluar.html', context)
      

def delete_surat_keluar(request , id_delete_surat_keluar):
    delete_surat = get_object_or_404(SemuaArsip, pk = id_delete_surat_keluar)
    upload_file   = SemuaArsip.objects.get(pk = id_delete_surat_keluar)

    if request.method == 'POST':
        upload_file.upload_file_arsip.delete()

        username = request.user
        group_name = str(Group.objects.get(user = username))


        get_surat       = request.POST.get('no_surat')
        get_kepada      = request.POST.get('kepada')
        get_tanggal     = request.POST.get('tanggal')
        get_perihal     = request.POST.get('prihal')
        get_klasifikasi = delete_surat.klasifikasi
        get_is_tu       = delete_surat.is_tu

        delete_surat = SemuaArsip(
             
            id                 = id_delete_surat_keluar,
            username           = str(username), 
            group              = group_name,
            no_surat           = get_surat, 
            kepada             = get_kepada,
            tgl_surat          = get_tanggal,
            perihal            = get_perihal, 
            klasifikasi        = get_klasifikasi,
            is_tu              = get_is_tu,
        )

        delete_surat.delete()
        return redirect('surat_keluar')   


    return render(request,'earsip/pages/surat/surat_keluar.html')


def simpan_ke_arsip(request, id_surat_keluar ):
        now = datetime.today()
        time_now = now.strftime("%Y-%m-%d")

        username = request.user
        group_name = Group.objects.get(user = username)
        group = str(group_name)

        surat = "Keluar"

        tempp_surat_keluar = SemuaArsip.objects.filter(group = group_name).values()
        # temp_surat_keluar = get_object_or_404(TempSuratKeluar)

        # Save to Arsip Database

        if request.method == 'POST':
            
            username          = request.user
            group_name        = str(Group.objects.get(user = username))

            get_surat         = str(surat)
            get_no_surat      = request.POST.get('no_surat')

            get_kepada        = request.POST.get('kepada')
            # get_surat_dari    = request.POST.get('surat_dari')
            
            get_tanggal       = request.POST.get('tanggal')
            get_perihal       = request.POST.get('prihal')
            get_klasifikasi   = request.POST.get('klasifikasi')

            get_tanggal_dibuat = time_now
            get_file_name      = tempp_surat_keluar.upload_file_arsip.file
            get_is_tu          = tempp_surat_keluar.is_tu
            
            
            simpan_surat = SemuaArsip(
                
                username           = str(username), 
                group              = group_name,
                surat              = get_surat,
                no_surat           = get_no_surat, 

                kepada             = get_kepada,
                tgl_surat          = get_tanggal,
                perihal            = get_perihal, 
                klasifikasi        = get_klasifikasi,
                tanggal_dibuat     = get_tanggal_dibuat,

                upload_file_arsip  = get_file_name, 
                is_tu              = get_is_tu,
            )

            print(simpan_surat)
            # edit_surat.save()

            return redirect('semua_surat')   



        return render(request,'earsip/pages/surat/surat_keluar.html')







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




