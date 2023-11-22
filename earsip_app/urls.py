from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("laporan/", views.laporan, name="laporan"),
    path("surat/", views.surat, name="surat"),
    path("tambah_surat/", views.tambah_surat, name="tambah_surat"),
    path("semua_surat/", views.semua_surat, name="semua_surat"),
    path("surat_harian/", views.surat_harian, name="surat_harian"),
    path("duplikat_surat/", views.duplikat_surat, name="duplikat_surat"),


    path("surat_terhapus/", views.surat_terhapus, name="surat_terhapus"),

    path("setting_klasifikasi/", views.setting_klasifikasi, name="setting_klasifikasi"),

    path("add_setting_klasifikasi/", views.add_setting_klasifikasi, name="add_setting_klasifikasi"),
    path('edit_setting_klasifikasi/<int:id_edit_klasifikasi>/', views.edit_setting_klasifikasi, name='edit_setting_klasifikasi'),
    path('delete_setting_klasifikasi/<int:id_delete_klasifikasi>/', views.delete_setting_klasifikasi, name='delete_setting_klasifikasi'),

    path("add_setting_subklasifikasi/", views.add_setting_subklasifikasi, name="add_setting_subklasifikasi"),
    # path('edit_setting_klasifikasi/<int:id_edit_klasifikasi>/', views.edit_setting_klasifikasi, name='edit_setting_klasifikasi'),
    # path('delete_setting_klasifikasi/<int:id_delete_klasifikasi>/', views.delete_setting_klasifikasi, name='delete_setting_klasifikasi'),
]
