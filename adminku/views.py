from django.shortcuts import render
import pyrebase

from .forms import Login, Admin
    


def index(request):
    login = Login()
    
    context = {
        'login_form': login,
    }
    
    return render(request, 'adminku/login.html', context)


def adminku(request):
    harga_mingguan = Admin()
    
    context = {
        'harga_mingguan':harga_mingguan,
    }
    return render(request, 'adminku/admin.html', context)