# Generated by Django 3.1.7 on 2021-05-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_color'),
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
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='account',
            name='color',
            field=models.CharField(default='212121', max_length=6),
        ),
    ]
