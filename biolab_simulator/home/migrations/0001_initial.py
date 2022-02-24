# Generated by Django 4.0.1 on 2022-02-24 00:20

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField(verbose_name='introduction')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('home_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.home')),
            ],
        ),
    ]
