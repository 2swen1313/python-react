# Generated by Django 4.0.5 on 2022-06-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=64)),
                ('button1', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Button2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field2', models.CharField(max_length=64)),
                ('button2', models.CharField(max_length=64)),
            ],
        ),
    ]