# Generated by Django 4.1 on 2022-09-01 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 1, 14, 14, 33, 166613, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
