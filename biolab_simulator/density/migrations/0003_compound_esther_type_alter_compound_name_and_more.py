# Generated by Django 4.0.1 on 2022-01-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('density', '0002_alter_absoluteparameter_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='esther_type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Esther type'),
        ),
        migrations.AlterField(
            model_name='compound',
            name='name',
            field=models.CharField(blank=True, default=1, max_length=50, verbose_name="Compound's representation"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equations',
            name='number',
            field=models.IntegerField(blank=True, verbose_name="Equation's number"),
        ),
        migrations.AlterField(
            model_name='graphs',
            name='label',
            field=models.CharField(blank=True, max_length=100, verbose_name="Graph's label"),
        ),
        migrations.DeleteModel(
            name='AbsoluteParameter',
        ),
    ]