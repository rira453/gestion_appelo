
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('ao.html', views.ao, name='ao'),
    path('contact.html', views.contact_view, name='contact'),
    path('marches.html', views.marches, name='marches'),
    path('reglements.html', views.reglements, name='reglements'),
    path('demarches.html', views.demarches, name='demarches'),
    path('false.html', views.false, name='false'),
    path('investissement.html', views.investissement, name='investissement'),
    path('contact.html', views.contact_view, name='contact'),
    path('thank_you.html', views.contact_view, name='thank_you'),
    path('admine.html', views.admine, name='admine'),
    path('login.html', views.user_login, name='login'),
     

    
    

    
    
]
