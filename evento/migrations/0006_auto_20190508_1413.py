# Generated by Django 2.2.1 on 2019-05-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0005_auto_20190508_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='link_evento',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
