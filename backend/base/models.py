from django.db import models 
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
#class participant
class Participant(models.Model):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_prenom = models.CharField(max_length=100)
    adress = models.TextField() 
    contact=models.CharField(max_length=20) 
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    #class client
class Client(models.Model):
    id_cl = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.TextField()
    contact = models.CharField(max_length=20)
    # On ne devrait pas nommer le champ de clé étrangère de la même manière que le modèle parent
    def __str__(self):
        return f"{self.nom} {self.prenom}"
#class event
class Event(models.Model):
    EVENT_TYPES = [
    ('Wedding', 'Wedding'),
    ('Birthday', 'Birthday'),
    ('Conference', 'Conference'),
    ('Graduation', 'Graduation'),
    ('Baptism', 'Baptism'),  
    ('Gender Reveal', 'Gender Reveal'),  
    # Ajoutez d'autres types d'événements selon vos besoins
]
    
    id_event = models.AutoField(primary_key=True)  # Identifiant auto-incrémenté pour l'événement
    title = models.CharField(max_length=100,default=None)
    type = models.CharField(max_length=100, choices=EVENT_TYPES)
    description = models.TextField(default=None)
    date = models.DateTimeField()
    adress = models.CharField(max_length=200)
    #participants = models.ManyToManyField(Participant)
   
    #client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
   
    def __str__(self):
        return f"{self.type} - {self.date}"

#class reservation
class Reservation(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'En attente'),
        ('Confirmed', 'Confirmée'),
        ('Cancelled', 'Annulée'),
    )

    num_res = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f"Réservation {self.num_res} - {self.get_status_display()}"
    #compte
class Compte(models.Model):
    num_compte = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)
    reservations = models.ManyToManyField(Reservation)

    def __str__(self):
        return f"Compte {self.num_compte} - {self.login}"
    #rapport
class Rapport(models.Model):
    num_rapp=models.AutoField(primary_key=True)
    date_rapp= models.DateField()
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f"Rapport {self.num_rapp}"
    #prestataire
class Prestataire(models.Model):
    class TypePrestataire(models.TextChoices):
        TRAITEUR = 'Traiteur', 'Traiteur'
        PHOTOGRAPHE = 'Photographe', 'Photographe'
        DJ = 'DJ', 'DJ'
        # Ajoutez d'autres types de prestataires selon vos besoins
    type = models.CharField(max_length=20, choices=TypePrestataire.choices,null=True)
    num_prestataire=models.AutoField(primary_key=True)
    nom_prestataire = models.CharField(max_length=100)   
    prenom_prestataire= models.CharField(max_length=100)
    num_tel=models.CharField(max_length=20) 

    Event = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f"{self.nom} {self.prenom}"

    #paiement
class Paiement(models.Model):
    id_paiement = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    # Définir les choix pour le mode de paiement
    CHOIX_MODE_PAIEMENT = (
        ('espece', 'Espèces'),
        ('carte', 'Carte de crédit'),
        ('cheque', 'Chèque'),
        ('virement', 'Virement bancaire'),
    )
    mode_de_paiement = models.CharField(max_length=100, choices=CHOIX_MODE_PAIEMENT)
    date = models.DateField()
    # Utilisation d'une clé étrangère pour lier les paiements aux clients
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return f"Paiement {self.id_paiement} - {self.client}"

    def __str__(self):
        return self.id_paiement
    #invitation
class Invitation(models.Model):
    STATUS_CHOICES = (
        ('En attente', 'En attente'),
        ('Acceptée', 'Acceptée'),
        ('Refusée', 'Refusée'),
    )

    num_invi = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En attente')
    adresse = models.CharField(max_length=255)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)

    def __str__(self):
        return f"Invitation {self.num_invi} - {self.nom}"
class Contact_us(models.Model):
        msg_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=70, default="")
        phone = models.CharField(max_length=70, default="")
        desc = models.CharField(max_length=500, default="")
        timestamp = models.DateTimeField(default=timezone.now)

        def _str_(self):
            return f"Contact {self.nom}"