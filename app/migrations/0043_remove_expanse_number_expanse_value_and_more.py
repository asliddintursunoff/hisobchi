# Generated by Django 5.1.6 on 2025-03-11 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_rename_datetime_dateforexpanse_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expanse',
            name='number',
        ),
        migrations.AddField(
            model_name='expanse',
            name='value',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 26, 22, 38, 1, 419083, tzinfo=datetime.timezone.utc)),
        ),
    ]
