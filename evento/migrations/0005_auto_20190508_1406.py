# Generated by Django 2.2.1 on 2019-05-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_auto_20190508_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='link_evento',
            field=models.CharField(blank=True, default='null', max_length=200, null=True),
        ),
    ]
