from django.contrib import admin

# Register your models here.

from .models import DatabaseSurat
from .models import DeleteSurat
from .models import KlasifikasiSurat
from .models import SubKlasifikasiSurat

class ListDatabaseSurat(admin.ModelAdmin):
    list_display = ('id','group', 'klasifikasi', 'subklasifikasi',
                    'tgl','no_surat','kepada','perihal',
                    'upload_file'
                    )

class ListDeleteSurat(admin.ModelAdmin):
    list_display = ('id','group', 'klasifikasi', 'subklasifikasi',
                    'tgl','no_surat','kepada','perihal',
                    'upload_file'
                    )
class ListKlasifikasiSurat(admin.ModelAdmin):
    list_display =  ('id','username','group', 'klasifikasi')

class ListSubKlasifikasiSurat(admin.ModelAdmin):
    list_display =  ('id','username','group' , 'subklasifikasi')


admin.site.register(DatabaseSurat,ListDatabaseSurat)
admin.site.register(DeleteSurat, ListDeleteSurat)
admin.site.register(KlasifikasiSurat, ListKlasifikasiSurat)
admin.site.register(SubKlasifikasiSurat,ListSubKlasifikasiSurat)