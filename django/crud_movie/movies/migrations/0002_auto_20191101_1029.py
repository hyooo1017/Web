# Generated by Django 2.2.6 on 2019-11-01 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='open_Date',
            new_name='open_date',
        ),
    ]
