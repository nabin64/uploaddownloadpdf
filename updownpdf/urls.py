

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.HOME, name='home'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('download_pdf/<int:pdf_id>/', views.DownloadPDF, name='download_pdf'),
    path('pdf_list/', views.pdf_list, name='pdf_list'),
]