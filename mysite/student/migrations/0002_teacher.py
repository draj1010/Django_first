# Generated by Django 3.0.5 on 2020-04-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.TextField()),
                ('name', models.TextField()),
                ('age', models.TextField()),
            ],
        ),
    ]
