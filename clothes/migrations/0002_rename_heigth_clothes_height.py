# Generated by Django 3.2.20 on 2024-03-18 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='heigth',
            new_name='height',
        ),
    ]
