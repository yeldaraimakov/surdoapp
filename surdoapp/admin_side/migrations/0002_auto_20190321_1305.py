# Generated by Django 2.1.5 on 2019-03-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surdoword',
            old_name='word',
            new_name='name',
        ),
    ]
