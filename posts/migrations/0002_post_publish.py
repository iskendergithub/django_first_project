# Generated by Django 4.1 on 2022-09-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
