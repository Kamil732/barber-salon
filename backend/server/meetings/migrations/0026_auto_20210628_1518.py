# Generated by Django 3.1.7 on 2021-06-28 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0037_auto_20210627_2331'),
        ('accounts', '0017_auto_20210615_1704'),
        ('meetings', '0025_auto_20210628_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='barber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='accounts.barber', verbose_name='Fryzjer'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='data.resource'),
        ),
    ]