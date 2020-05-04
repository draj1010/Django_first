# Generated by Django 3.0.5 on 2020-05-04 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20200504_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='orm.Customer'),
        ),
    ]