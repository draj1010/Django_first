# Generated by Django 3.0.5 on 2020-04-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.TextField()),
                ('sku', models.TextField()),
                ('price', models.TextField()),
                ('desc', models.TextField()),
                ('slug', models.TextField()),
            ],
        ),
    ]
