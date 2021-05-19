from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#Se crea una form para insertar info de un customer en la base de datos. 


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

#Funciona bien hasta aca. 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 
