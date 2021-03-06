# Generated by Django 2.2.1 on 2019-05-08 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulario', '0004_delete_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='AULA',
            fields=[
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_autor', models.CharField(max_length=50)),
                ('email_autor', models.EmailField(blank=True, max_length=100, null=True)),
                ('titulo_atividade', models.CharField(max_length=50)),
                ('data_criação', models.DateTimeField(auto_now=True)),
                ('data_edição', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
