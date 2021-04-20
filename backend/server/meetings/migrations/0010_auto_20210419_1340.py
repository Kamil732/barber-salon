# Generated by Django 3.1.7 on 2021-04-19 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetings', '0009_auto_20210415_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='customer_fax_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Zapasowy numer telefonu klienta'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='customer_last_name',
            field=models.CharField(default='Głuchowski', max_length=20, verbose_name='Nazwisko klienta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='customer_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+48500484315', max_length=128, region=None, verbose_name='Numer telefonu klienta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='barber',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='Fryzjer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='meetings', to=settings.AUTH_USER_MODEL, verbose_name='Konto klienta'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='customer_first_name',
            field=models.CharField(max_length=20, verbose_name='Imię klienta'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('hair', 'Włosy'), ('beard', 'Broda'), ('do_not_work', 'NIE PRACUJE')], max_length=11, verbose_name='Typ wizyty'),
        ),
    ]