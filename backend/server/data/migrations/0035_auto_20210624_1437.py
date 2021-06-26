# Generated by Django 3.1.7 on 2021-06-24 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0034_serviceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('black', 'Czarny'), ('light-blue', 'Jasny niebieski'), ('blue', 'Niebieski'), ('light-green', 'Jasny Zielony'), ('green', 'Zielony'), ('pink', 'Różowy'), ('purple', 'Fioletowy'), ('brown', 'Brązowy'), ('yellow', 'Żółty'), ('orange', 'Pomarańczowy')], default='Czarny', max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resources', models.ManyToManyField(related_name='services', to='data.Resource')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='data.service')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='data.resourcegroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='data.resourcegroup'),
        ),
    ]