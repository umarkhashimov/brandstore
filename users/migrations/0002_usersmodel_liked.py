# Generated by Django 5.2.1 on 2025-06-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_produtsmodel'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='liked',
            field=models.ManyToManyField(to='products.produtsmodel'),
        ),
    ]
