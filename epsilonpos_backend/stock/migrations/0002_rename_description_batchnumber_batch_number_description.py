# Generated by Django 4.0.4 on 2022-06-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batchnumber',
            old_name='description',
            new_name='batch_number_description',
        ),
    ]
