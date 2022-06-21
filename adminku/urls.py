from django.urls import path

from . import views

urlpatterns = [
    path(r'login/', views.index, name='login'),
    path(r'admin/',views.adminku, name='admin')
]