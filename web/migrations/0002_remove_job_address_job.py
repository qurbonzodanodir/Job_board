# Generated by Django 4.2 on 2024-03-19 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='address_job',
        ),
    ]
