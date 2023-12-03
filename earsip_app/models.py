from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.group}/surat/{filename}"

# def user_folder(instance, filename):
#     return f"{instance.group}/surat/{filename}"

# def user_folder(instance, filename):
#     return f"{instance.group}/surat/{filename}"

# def user_folder(instance, filename):
#     return f"{instance.group}/surat/{filename}"

# class CustomUser(AbstractUser):
#     pass


# def add_user_to_groups(sender, instance, **kwargs):
#     group_names = ['Group1', 'Group2', 'Group3']

#     # Add the user to the specified groups
#     for group_name in group_names:
#         group, created = Group.objects.get_or_create(name=group_name)
#         instance.groups.add(group)

#     models.signals.post_save.connect(add_user_to_groups, sender=CustomUser)


class SemuaArsip(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=20)

    surat = models.CharField(max_length=10  , null=True)
    surat_dari = models.CharField(max_length=30, null=True)

    no_surat = models.CharField(max_length=20)
    kepada = models.CharField(max_length=200)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=200)
    klasifikasi = models.CharField(max_length=30)
    tanggal_dibuat = models.DateField()
    upload_file_arsip = models.FileField(upload_to= user_folder, null=False, blank=False)
    is_read = models.CharField(max_length=2, null=True)
    is_tu = models.IntegerField(null = True)
    is_spri = models.CharField(max_length=2 , null=True)
    is_admin = models.CharField(max_length=2 , null=True)

    def __str__(self):
        return self.no_surat
    class Meta:
        db_table = "SemuaArsip"

class Disposisi(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    no_surat  = models.ForeignKey(SemuaArsip , on_delete = models.CASCADE)
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

# class TempDisposisi(models.Model):

#     id = models.AutoField(primary_key=True, unique=True)
#     no_surat  = models.ForeignKey(SemuaArsip , on_delete = models.PROTECT)
#     no_agenda  = models.TextField(max_length=40)
#     notes      = models.TextField(max_length=200)
#     username = models.CharField(max_length=30)
#     group = models.CharField(max_length=20)
#     upload_file_agenda = models.FileField(upload_to= user_folder, null=False, blank=False)
#     is_read = models.CharField(max_length=2)

#     def __str__(self):
#         return self.no_agenda
#     class Meta:
#         db_table = "TempDisposisi"

# class TempSuratKeluar(models.Model):
  
#     id = models.AutoField(primary_key=True, unique=True)
#     username = models.CharField(max_length=30)
#     group = models.CharField(max_length=20)
#     no_surat = models.CharField(max_length=20)
#     kepada = models.CharField(max_length=200)
#     tgl_surat = models.DateField()
#     perihal = models.CharField(max_length=200)
#     klasifikasi = models.CharField(max_length=30)
#     upload_file_arsip = models.FileField(upload_to= user_folder, null=False, blank=False)
#     is_tu = models.IntegerField()

#     class Meta:
#         db_table = "TempSuratKeluar"



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

        



