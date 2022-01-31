# Generated by Django 3.2 on 2022-01-31 16:37

from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'app/fixture/user.json', app_label='app')

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(load_fixture),
    ]
