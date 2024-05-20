from django.shortcuts import render
from .forms import ContactForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Header and footer view 
def index(request):
    return render(request,'index.html')
def ao(request):
    return render(request,'ao.html')

def reglements(request):
    return render(request,'reglements.html')
def false(request):
    return render(request,'false.html')
def marches(request):
    return render(request,'marches.html')
def demarches(request):
    return render(request,'demarches.html')
def investissement(request):
    return render(request,'investissement.html')
def doc(request):
    return render(request,'doc.html')
def admine(request):
    return render(request,'admine.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = ContactRequest(
                type_of_request=form.cleaned_data['type_of_request'],
                company_name=form.cleaned_data['company_name'],
                industry=form.cleaned_data['industry'],
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                observations=form.cleaned_data['observations']
            )
            contact_request.save()
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def ao(request):
    data = TableData.objects.all()
    return render(request, 'ao.html', {'data': data})






def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            login(request, user)
           
            return redirect('index')  
        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
         
           
    else:
     return render(request, 'login.html')


