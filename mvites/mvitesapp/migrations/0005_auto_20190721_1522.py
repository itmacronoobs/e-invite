# Generated by Django 2.2.3 on 2019-07-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvitesapp', '0004_auto_20190720_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='endtime',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='starttime',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
