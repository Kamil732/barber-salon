# Generated by Django 3.1.7 on 2021-06-01 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0028_auto_20210531_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicegroup',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='data.servicegroup'),
        ),
        migrations.AlterUniqueTogether(
            name='servicegroup',
            unique_together={('parent',)},
        ),
    ]
