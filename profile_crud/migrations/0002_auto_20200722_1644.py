# Generated by Django 3.0.8 on 2020-07-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
