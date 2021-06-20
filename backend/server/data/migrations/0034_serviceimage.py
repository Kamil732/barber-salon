# Generated by Django 3.1.7 on 2021-06-10 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_auto_20210610_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_images/%Y/%m/%d/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='data.service')),
            ],
        ),
    ]