# Generated by Django 4.0.1 on 2022-03-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('density', '0006_rename_model_id_parameter_compound_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictivemodel',
            name='brief_description',
            field=models.CharField(default='test', max_length=500, verbose_name='Brief description for home page'),
            preserve_default=False,
        ),
    ]
