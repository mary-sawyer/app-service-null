# Generated by Django 2.0.7 on 2018-07-14 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0005_vol_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vol_info',
            name='skills',
            field=models.CharField(max_length=1000),
        ),
    ]