# Generated by Django 3.1.6 on 2021-02-19 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='appointment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.appointment'),
        ),
    ]
