# Generated by Django 5.1.3 on 2025-03-30 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planodetreino',
            name='dataFim',
        ),
    ]
