# Generated by Django 2.0.3 on 2018-05-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]