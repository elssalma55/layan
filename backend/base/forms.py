from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput,TextInput
from django import forms
from . models import  Event,Reservation

 
#create user
class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
#login user
class loginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    # Dans votre fichier forms.py



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'type', 'description', 'date', 'adress']
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'status', 'client']
        

