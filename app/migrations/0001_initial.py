# Generated by Django 3.2 on 2022-08-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('doj', models.DateField(blank=True, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('post', models.CharField(max_length=100, null=True)),
                ('addess', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('leave_count', models.IntegerField(blank=True, default=0, null=True)),
                ('on_leave', models.BooleanField(default=False)),
            ],
        ),
    ]