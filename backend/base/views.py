from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseBadRequest
from . forms import createUserForm ,loginForm ,EventForm,ReservationForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Participant, Client, Event, Reservation, Compte, Rapport, Prestataire, Paiement, Invitation, Contact_us 
import datetime
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.models import auth#a function that will allow us to logout
from django.contrib.auth import authenticate#a function that will allow us to authentificate our user
from django.contrib.auth.decorators import login_required # will ensure that authentificqted have access to the right pages


def home(request):
   
   return render(request,'base/base.html')
#inscription
def registrer(request):
   
   form=createUserForm()
   if request.method == "POST":
        
        form = createUserForm(request.POST)
        if form.is_valid():
                
            form.save()
            
            return redirect("connexion")
    
   context = {'form':form}
    
   return render(request,'base/registrer.html',context=context)
#connexion
def connexion(request):
    form = loginForm()
    context = {'form': form}  # Définir un contexte par défaut

    if request.method == "POST":
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password') 
            
            user = authenticate(request, username=username, password=password)
                
            if user is not None:
                auth.login(request, user)
                # Vous pouvez effectuer d'autres opérations ici si l'authentification réussit
                # Par exemple, rediriger l'utilisateur vers une autre vue
                return redirect('our_events')
            else:
                # Ajouter un message d'erreur dans le contexte si l'authentification échoue
                context['login_error'] = True

    # Retourner le rendu du template avec le contexte, quel que soit le résultat de l'authentification
    return render(request, 'base/connexion.html', context=context)
#déconnexion
def deconnexion(request):
    auth.logout(request)
     
    return redirect("connexion")
    
#tab de bord
@login_required(login_url='connexion')
def dashboard(request):
    my_clients= Client.objects.all()
    context={'my_clients': my_clients} 
    return render(request, 'base/dashboard.html ',context=context)
@login_required(login_url='connexion')
#our_events
def our_events(request):
   
   return render(request,'base/our_events.html')
#mariage
def mariage(request):
   
   return render(request,'base/mariage.html')
# Dans votre fichier views.py

#event form
from .forms import EventForm
@login_required(login_url='connexion')
def our_events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    else:
        form = EventForm()
    return render(request, 'base/our_events.html', {'form': form})
def birthday(request):
   
   return render(request,'base/birthday.html')
def gender_reveal(request):
   
   return render(request,'base/gender_reveal.html')

def conference(request):
   
   return render(request,'base/conference.html')
def graduation(request):
   
   return render(request,'base/graduation.html')
def baptism(request):
   
   return render(request,'base/baptism.html')
#reservation form
@login_required(login_url='connexion')
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your reservation has been successfully made!")  # Ajouter un message de succès
            return redirect('reservation')
    else:
        form = ReservationForm()
    return render(request, 'base/reservation.html', {'form': form})
def contact_us(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact_us(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'base/contact_us.html', {'thank': thank})
    return render(request, 'base/contact_us.html', {'thank': thank})

