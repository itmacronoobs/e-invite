# Generated by Django 2.2.3 on 2019-07-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvitesapp', '0002_itinerary_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='eventdatetime',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='eventendtime',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='eventstarttime',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
