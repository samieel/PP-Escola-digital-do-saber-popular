# Generated by Django 2.2.1 on 2019-05-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0042_auto_20190526_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='titulo_aula',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
