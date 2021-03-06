# Generated by Django 2.1.5 on 2019-04-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0002_auto_20190321_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surdoword',
            old_name='name',
            new_name='name_kz',
        ),
        migrations.AddField(
            model_name='surdoword',
            name='name_ru',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surdoword',
            name='category',
            field=models.IntegerField(choices=[(0, 'Время, календарь'), (1, 'Алфавит'), (2, 'Знакомство'), (3, 'Человек'), (4, 'Семья'), (5, 'Названия месяцев'), (6, 'Дни недели'), (7, 'Природа'), (8, 'Времена года')], default=0),
        ),
        migrations.AlterField(
            model_name='surdoword',
            name='video_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
