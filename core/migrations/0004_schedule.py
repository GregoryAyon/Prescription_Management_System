# Generated by Django 3.1.5 on 2021-02-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Saturday', models.CharField(max_length=122)),
                ('Sunday', models.CharField(max_length=122)),
                ('Monday', models.CharField(max_length=122)),
                ('Tuesday', models.CharField(max_length=122)),
                ('Wednesday', models.CharField(max_length=122)),
                ('Thursday', models.CharField(max_length=122)),
                ('limit', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
