# Generated by Django 4.2 on 2023-06-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reja',
            name='vaqt',
            field=models.TimeField(blank=True, null=True),
        ),
    ]