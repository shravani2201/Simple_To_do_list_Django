# Generated by Django 4.2.6 on 2024-06-23 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
