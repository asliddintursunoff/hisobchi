# Generated by Django 5.1.6 on 2025-02-26 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_company_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 13, 20, 1, 5, 938849, tzinfo=datetime.timezone.utc)),
        ),
    ]
