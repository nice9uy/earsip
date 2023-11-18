from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('test/', views.test, name ='test'),
]