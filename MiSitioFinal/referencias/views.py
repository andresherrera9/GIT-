from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Referencias
from django.db.models import Q
from .forms import CustomerForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout


def referencia(request):
    subpartida =  Referencias.objects.all()
    return render(request, 'home.html', {'subpartida' : subpartida})



def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(idreferencias__icontains=query) |
            Q(referencia__icontains=query) |
            Q(marca__icontains=query)|
            Q(subpartida__icontains=query) 
            
        )
        results = Referencias.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response ("referencias/search.html",{
        "results" : results,
        "query" : query
        })

# Se crea la view.index para realizar una form. Se referencia al template index.html
# donde se llama a {{form}} que llama a CustomerForm que lleva a form.py  que llama el modelo Customer
# que esta en models.py que crea una base de datos donde se guardara la info del customer

def index(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST) 
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'referencias/index.html', context)

#Se va a intentar crear una registration form. 

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user )
            return redirect('login')


    context = {'form':form}
    return render(request, 'referencias/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request,user)
            return redirect('search')

        
    context = {}
    return render(request, 'referencias/login.html',context)




