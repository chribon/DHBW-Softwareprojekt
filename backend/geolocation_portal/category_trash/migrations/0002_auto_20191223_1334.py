# Generated by Django 3.0 on 2019-12-23 12:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0009_auto_20191223_1334'),
        ('category_trash', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothingentry',
            options={'verbose_name': 'Altkleidersammelstelle', 'verbose_name_plural': 'Altkleidersammelstellen'},
        ),
        migrations.CreateModel(
            name='RecyclingcentreEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=6, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Wertstoffhof',
                'verbose_name_plural': 'Wertstoffhöfe',
            },
        ),
        migrations.CreateModel(
            name='IlluminantEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Leuchtmittelsammelstelle',
                'verbose_name_plural': 'Leuchtmittelsammelstelle',
            },
        ),
        migrations.CreateModel(
            name='ElectroEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Elektroschrottsammelstelle',
                'verbose_name_plural': 'Elektroschrottsammelstellen',
            },
        ),
        migrations.CreateModel(
            name='BatteryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Batteriesammelstelle',
                'verbose_name_plural': 'Batteriesammelstellen',
            },
        ),
    ]
