# Generated by Django 4.0.6 on 2022-07-08 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='Home name')),
                ('intro', models.TextField(verbose_name='Introduction')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('home_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.home')),
            ],
        ),
    ]
