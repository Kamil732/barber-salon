# Generated by Django 3.1.7 on 2021-04-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210327_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='customer_images/%Y/%m/%d/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
