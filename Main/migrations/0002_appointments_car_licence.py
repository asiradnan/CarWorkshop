# Generated by Django 4.2.11 on 2024-12-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='car_licence',
            field=models.CharField(default='', max_length=200),
        ),
    ]