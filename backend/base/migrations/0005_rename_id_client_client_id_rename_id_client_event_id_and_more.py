# Generated by Django 5.0.4 on 2024-05-01 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_id_client_id_client_remove_client_id_event_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='id_client',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='id_client',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='id_client',
            new_name='id',
        ),
    ]
