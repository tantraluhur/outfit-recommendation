# Generated by Django 3.2.20 on 2024-03-19 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
        ('clothes', '0003_alter_segmentation_clothes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='dataset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataset.dataset'),
        ),
    ]