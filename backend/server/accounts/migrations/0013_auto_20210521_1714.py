# Generated by Django 3.1.7 on 2021-05-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210521_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bookings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='no_shows',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='revenue',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='trusted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]