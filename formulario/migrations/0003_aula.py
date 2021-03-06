# Generated by Django 2.2.1 on 2019-05-06 19:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulario', '0002_delete_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='AULA',
            fields=[
                ('aul_codigo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('aul_nome', models.CharField(max_length=50)),
                ('aul_titulo', models.CharField(max_length=50)),
                ('aul_data', models.DateTimeField(auto_now=True)),
                ('aul_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('aul_imagem', models.FileField(blank=True, null=True, upload_to='fotos/')),
            ],
        ),
    ]
