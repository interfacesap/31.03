# Generated by Django 4.0.1 on 2022-03-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tipoatv'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentralTrab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCentralTrab', models.CharField(max_length=20)),
            ],
        ),
    ]
