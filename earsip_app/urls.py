from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tambah_surat/", views.tambah_surat, name="tambah_surat"),

    path("surat_keluar/", views.surat_keluar, name="surat_keluar"),
    path('edit_surat_keluar/<int:id_edit_surat_keluar>/', views.edit_surat_keluar, name='edit_surat_keluar'),
    path('delete_surat_keluar/<int:id_delete_surat_keluar>/', views.delete_surat_keluar, name='delete_surat_keluar'),

    path("simpan_ke_arsip/", views.simpan_ke_arsip, name="simpan_ke_arsip"),
    # path("surat/", views.surat, name="surat"),
    # path("semua_surat/", views.semua_surat, name="semua_surat"),
    # path("duplikat_surat/", views.duplikat_surat, name="duplikat_surat"),

    

    # path("surat_keluar/", views.surat_keluar, name="surat_keluar"),








    # path("surat_terhapus/", views.surat_terhapus, name="surat_terhapus"),

    # path("setting_klasifikasi/", views.setting_klasifikasi, name="setting_klasifikasi"),

    # path("add_setting_klasifikasi/", views.add_setting_klasifikasi, name="add_setting_klasifikasi"),
    # path('edit_setting_klasifikasi/<int:id_edit_klasifikasi>/', views.edit_setting_klasifikasi, name='edit_setting_klasifikasi'),
    # path('delete_setting_klasifikasi/<int:id_delete_klasifikasi>/', views.delete_setting_klasifikasi, name='delete_setting_klasifikasi'),

    # path("add_setting_subklasifikasi/", views.add_setting_subklasifikasi, name="add_setting_subklasifikasi"),
    # path('edit_setting_subklasifikasi/<int:id_edit_setting_subklasifikasi>/', views.edit_setting_subklasifikasi, name='edit_setting_subklasifikasi'),
    # path('delete_setting_subklasifikasi/<int:id_delete_setting_subklasifikasi>/', views.delete_setting_subklasifikasi, name='delete_setting_subklasifikasi'),
]
