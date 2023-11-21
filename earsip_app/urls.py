from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("laporan/", views.laporan, name="laporan"),
    path("surat/", views.surat, name="surat"),
    path("tambah_surat/", views.tambah_surat, name="tambah_surat"),
    path("semua_surat/", views.semua_surat, name="semua_surat"),
]
