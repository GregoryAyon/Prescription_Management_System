# Generated by Django 3.2 on 2021-04-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_doctor_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='check_status',
            field=models.CharField(choices=[('Visited', 'Visited'), ('Unvisited', 'Unvisited')], default='Unvisited', max_length=122, null=True),
        ),
    ]