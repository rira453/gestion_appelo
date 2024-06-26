# Generated by Django 5.0.6 on 2024-05-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_request', models.CharField(choices=[('info', "Demande d'info"), ('other', 'Autre demande')], max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('observations', models.TextField()),
            ],
        ),
    ]
