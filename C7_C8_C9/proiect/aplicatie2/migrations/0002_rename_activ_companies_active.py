# Generated by Django 4.0.4 on 2022-05-08 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='activ',
            new_name='active',
        ),
    ]