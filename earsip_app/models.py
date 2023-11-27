from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.username}/surat/{filename}"

class SekretariatDb(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "SekretariatDb"

class SekretariatDisposisi(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "SekretariatDisposisi"

####################################################################################################  End Sekretariat

class PusalpalhanDb(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusalpalhanDb"

class PusalpalhanDisposisi(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusalpalhanDisposisi"


####################################################################################################  End Pusalpalhan


class PuskonDb(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PuskonDb"

class PuskonDisposisi(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PuskonDisposisi"



####################################################################################################  End PusKon

class PusKodDb(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusKodDb"

class PusKodDisposisi(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusKodDisposisi"


####################################################################################################  End PusKod

class PusBmnDb(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusBmnDb"

class PusBmnDisposisi(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "PusBmnDisposisi"


####################################################################################################  End PusKod

class KlasifikasiSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)
    class Meta:
        db_table = "KlasifikasiSurat"

class TempSuratMasuk(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    klasifikasi = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    
    class Meta:
        db_table = "TempSuratMasuk"


class TempSuratKeluar(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    klasifikasi = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    
    class Meta:
        db_table = "SuratKeluar"
        
class DeleteSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    klasifikasi = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    
    class Meta:
        db_table = "DeleteSurat"

class DisposisiSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_agenda  = models.TextField(max_length=200)
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    status_surat = models.CharField(max_length=200)
    tanggal_dibuat = models.DateField()
    
    class Meta:
        db_table = "DisposisiSurat"


