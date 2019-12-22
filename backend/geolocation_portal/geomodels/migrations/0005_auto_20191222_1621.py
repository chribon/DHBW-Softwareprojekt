# Generated by Django 3.0 on 2019-12-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0004_auto_20191220_0011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GlassTrash',
            new_name='GlassTrashEntry',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='entry_types',
            field=models.CharField(choices=[('glasstrash', 'Glassmüll-Abgabestellen'), ('clothing', 'Altkleider-Abgabestellen'), ('batterytrash', 'Altbatterien-Abgabestellen')], default='glasstrash', max_length=30, verbose_name='Art der möglichen Einträge'),
        ),
    ]
