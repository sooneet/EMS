# Generated by Django 3.2 on 2022-08-06 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='addess',
            new_name='address',
        ),
    ]
