# Generated by Django 3.1.7 on 2021-03-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20210327_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='account',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='meeting',
            name='customer_first_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Imię Klienta'),
        ),
    ]
