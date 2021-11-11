# Generated by Django 3.2.9 on 2021-11-11 22:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20211108_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 22, 46, 4, 311598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]
