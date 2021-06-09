# Generated by Django 3.1.7 on 2021-05-31 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0026_service_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='barbers',
        ),
        migrations.AddField(
            model_name='service',
            name='vat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='data.servicegroup'),
        ),
    ]
