# Generated by Django 3.0.8 on 2020-07-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff status'),
        ),
    ]
