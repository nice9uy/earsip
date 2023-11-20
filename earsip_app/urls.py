from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("laporan/", views.laporan, name="laporan"),
    path("surat/", views.surat, name="surat"),
]
