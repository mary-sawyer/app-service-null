# Generated by Django 2.0.7 on 2018-07-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0011_vol_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vol_info',
            name='location',
            field=models.CharField(choices=[('SC', 'SC'), ('FR', 'FR'), ('South San Jose', 'South San Jose'), ('West san jose', 'West san jose'), ('East San Jose', 'East San Jose'), ('Milpitas', 'Milpitas'), ('Mountain View', 'Mountain View'), ('palo alto', 'palo alto'), ('melon park', 'melon park')], max_length=255),
        ),
    ]