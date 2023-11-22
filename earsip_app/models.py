from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.username}/surat/{filename}"

class DatabaseSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    klasifikasi = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    
    class Meta:
        db_table = "DatabaseSurat"

class DeleteSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    klasifikasi = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    
    class Meta:
        db_table = "DeleteSurat"


class KlasifikasiSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "KlasifikasiSurat"


class SubKlasifikasiSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    subklasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "SubKlasifikasiSurat"