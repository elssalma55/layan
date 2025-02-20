# Generated by Django 5.0.4 on 2024-05-03 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_paiement_id_alter_paiement_id_paiement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('num_invi', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('statut', models.CharField(choices=[('En attente', 'En attente'), ('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')], default='En attente', max_length=20)),
                ('adresse', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.participant')),
            ],
        ),
    ]
