# Generated by Django 2.2.1 on 2019-05-08 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0015_auto_20190508_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 8, 13, 45, 28, 958501)),
        ),
    ]