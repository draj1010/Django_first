# Generated by Django 3.0.5 on 2020-05-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
