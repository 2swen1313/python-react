# Generated by Django 4.0.5 on 2022-06-17 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buttonapp', '0002_button_delete_button1_delete_button2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='button',
            name='button1',
        ),
        migrations.RemoveField(
            model_name='button',
            name='button2',
        ),
        migrations.RemoveField(
            model_name='button',
            name='field2',
        ),
    ]
