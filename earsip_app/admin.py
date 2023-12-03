from django.contrib import admin

# Register your models here.

from .models import SemuaArsip
from .models import Disposisi
# from .models import TempSuratKeluar
from .models import KlasifikasiSurat

class ListDisposisi(admin.ModelAdmin):
    list_display = ('id','no_surat','no_agenda','notes',
                    'username', 'group', 'upload_file_agenda',
                    'is_read'
                    )

# # class ListFileArsip(admin.ModelAdmin):
# #     list_display = ('no_surat','username', 'group')

class ListSemuaArsip(admin.ModelAdmin):
    list_display =  ('id','username','group', 'surat','no_surat',
                     'kepada','tgl_surat',
                     'perihal','klasifikasi','tanggal_dibuat',
                     'upload_file_arsip','is_read','is_tu','is_admin'
                     )
    
# class ListTempSuratKeluar(admin.ModelAdmin):
#     list_display =  ('id','username','group', 'no_surat',
#                      'kepada','tgl_surat',
#                      'perihal','klasifikasi',
#                      'upload_file_arsip','is_tu'
                    
#                      )

class ListKlasifikasiSurat(admin.ModelAdmin):
    list_display = ('id','klasifikasi')


admin.site.register(Disposisi , ListDisposisi)
# admin.site.register(FileArsip , ListFileArsip)
admin.site.register(SemuaArsip , ListSemuaArsip)
# admin.site.register(TempSuratKeluar , ListTempSuratKeluar)
admin.site.register(KlasifikasiSurat , ListKlasifikasiSurat)

