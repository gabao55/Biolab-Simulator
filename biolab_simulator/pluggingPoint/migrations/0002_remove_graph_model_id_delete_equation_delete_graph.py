# Generated by Django 4.1.1 on 2022-10-05 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pluggingPoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='model_id',
        ),
        migrations.DeleteModel(
            name='Equation',
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
    ]
