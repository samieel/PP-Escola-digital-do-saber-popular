# Generated by Django 2.2.1 on 2019-05-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0007_remove_evento_link_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='link_evento',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
