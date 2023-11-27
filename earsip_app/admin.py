from django.contrib import admin

# Register your models here.

from .models import SekretariatDb
from .models import SekretariatDisposisi

from .models import PusalpalhanDb
from .models import PusalpalhanDisposisi

from .models import PuskonDb
from .models import PuskonDisposisi

from .models import PusKodDb
from .models import PusKodDisposisi

from .models import PusBmnDb
from .models import PusBmnDisposisi
############################################
from .models import KlasifikasiSurat
from .models import TempSuratMasuk
from .models import TempSuratKeluar
from .models import DeleteSurat
############################################





admin.site.register(SekretariatDb)
admin.site.register(SekretariatDisposisi)

admin.site.register(PusalpalhanDb)
admin.site.register(PusalpalhanDisposisi)

admin.site.register(PuskonDb)
admin.site.register(PuskonDisposisi)

admin.site.register(PusKodDb)
admin.site.register(PusKodDisposisi)

admin.site.register(PusBmnDb)
admin.site.register(PusBmnDisposisi)
##########################################
admin.site.register(KlasifikasiSurat)
admin.site.register(TempSuratMasuk)
admin.site.register(TempSuratKeluar)
admin.site.register(DeleteSurat)






# from .models import DatabaseSurat
# from .models import DeleteSurat
# from .models import KlasifikasiSurat
# from .models import SubKlasifikasiSurat

# class ListDatabaseSurat(admin.ModelAdmin):
#     list_display = ('id','group', 'klasifikasi', 'subklasifikasi',
#                     'tgl','no_surat','kepada','perihal',
#                     'upload_file'
#                     )

# class ListDeleteSurat(admin.ModelAdmin):
#     list_display = ('id','group', 'klasifikasi', 'subklasifikasi',
#                     'tgl','no_surat','kepada','perihal',
#                     'upload_file'
#                     )
# class ListKlasifikasiSurat(admin.ModelAdmin):
#     list_display =  ('id','username','group', 'klasifikasi')

# class ListSubKlasifikasiSurat(admin.ModelAdmin):
#     list_display =  ('id','username','group' , 'subklasifikasi')


# admin.site.register(DatabaseSurat)
# admin.site.register(DeleteSurat)
# admin.site.register(KlasifikasiSurat)
# admin.site.register(SubKlasifikasiSurat)