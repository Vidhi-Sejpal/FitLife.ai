# Generated by Django 3.2 on 2022-02-21 04:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_playlist_check_current_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist_check',
            name='current_date',
            field=models.DateField(default=datetime.date(2022, 2, 21)),
        ),
    ]
