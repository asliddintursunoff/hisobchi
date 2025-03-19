# Generated by Django 5.1.6 on 2025-03-06 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_company_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence_date',
            name='day',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 19, 50, 40, 264399, tzinfo=datetime.timezone.utc)),
        ),
    ]
