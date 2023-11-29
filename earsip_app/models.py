from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.group}/surat/{filename}"

def user_folder(instance, filename):
    return f"{instance.group}/surat/{filename}"

def user_folder(instance, filename):
    return f"{instance.group}/surat/{filename}"

def user_folder(instance, filename):
    return f"{instance.group}/surat/{filename}"


class SemuaArsip(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    surat = models.CharField(max_length=10)
    no_surat = models.CharField(max_length=20)
    kepada = models.CharField(max_length=200)
    surat_dari = models.CharField(max_length=30)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    tanggal_dibuat = models.DateField()
    upload_file_arsip = models.FileField(upload_to= user_folder, null=False, blank=False)
    is_read = models.CharField(max_length=2)
    is_tu = models.CharField(max_length=2)
    is_admin = models.CharField(max_length=2)

    def __str__(self):
        return self.no_surat
    class Meta:
        db_table = "SemuaArsip"

class Disposisi(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    no_surat  = models.ForeignKey(SemuaArsip , on_delete = models.PROTECT)
    no_agenda  = models.TextField(max_length=40)
    notes      = models.TextField(max_length=200)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    upload_file_agenda = models.FileField(upload_to= user_folder, null=False, blank=False)
    is_read = models.CharField(max_length=2)

    def __str__(self):
        return self.no_agenda
    class Meta:
        db_table = "Disposisi"

class TempSuratKeluar(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    no_surat = models.CharField(max_length=20)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    upload_file_arsip = models.FileField(upload_to= user_folder, null=False, blank=False)
    

    
    class Meta:
        db_table = "SuratKeluar"

class KlasifikasiSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    klasifikasi = models.CharField(max_length=30)
    class Meta:
        db_table = "KlasifikasiSurat"

class ChecklistSubBag(models.Model):
    bag = models.CharField(max_length=30)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

        



