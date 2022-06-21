from django.urls import path

from . import views

urlpatterns = [
    path('link-aja/', views.pay, name='linkAja'),
    path('dana/', views.pay, name='dana'),
    path('bni/', views.pay, name='bni'),
    
    
]