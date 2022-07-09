
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    # path('admin/', admin.site.urls),
    path(r'', views.index,name='home'),
    path(r'', include('paygate.urls'),name='linkAja'),
    path(r'', include('paygate.urls'),name='bni'),
    path(r'', include('paygate.urls'),name='dana'),
    path(r'', include('adminku.urls'),name='login'),
    path(r'', include('adminku.urls'),name='admin'),
]
