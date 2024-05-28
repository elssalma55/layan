


from django.urls import path
from .views import *
from django import views
from base import views
urlpatterns = [
    path('', home, name=''),  # Nommez votre vue 'home'
    path('registrer', registrer, name='registrer'),  # Nommez votre vue 'registrer'
    path('connexion', connexion, name='connexion'),
    path('deconnexiom', deconnexion, name='deconnexion'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('our_events',our_events, name='our_events'),
    path('mariage',mariage, name='mariage'),
    path('our_events', our_events, name='our_events'),
    path('reservation', reservation, name='reservation'),
    path('birthday',birthday, name='birthday'),
    path('gender_reveal',gender_reveal, name='gender_reveal'),
    path('conference',conference, name='conference'),
    path('graduation',graduation, name='graduation'),
    path('baptism',baptism, name='baptism'),
    path('contact_us', contact_us, name="contact_us"),
   
   
    # Autres URLs...
]

  

