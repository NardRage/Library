# Generated by Django 2.2.10 on 2021-07-26 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_auto_20210726_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='member',
            name='expired',
        ),
        migrations.AddField(
            model_name='member',
            name='created_by',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 19, 38, 54, 779764)),
        ),
    ]