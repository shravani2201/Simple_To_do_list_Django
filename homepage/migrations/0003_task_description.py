# Generated by Django 4.2.6 on 2024-06-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_remove_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
