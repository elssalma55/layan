# Generated by Django 5.0.4 on 2024-05-03 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='reservations',
            field=models.ManyToManyField(to='base.reservation'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.client'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='login',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='compte',
            name='mot_de_passe',
            field=models.CharField(max_length=100),
        ),
    ]
