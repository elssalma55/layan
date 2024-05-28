from django.contrib import admin

# Register your models here.
from .models import Participant, Client, Event, Reservation, Compte, Rapport, Prestataire, Paiement, Invitation



admin.site.register(Participant)

admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Reservation)
admin.site.register(Compte)
admin.site.register(Rapport)
admin.site.register(Prestataire)
admin.site.register(Paiement)
admin.site.register(Invitation)