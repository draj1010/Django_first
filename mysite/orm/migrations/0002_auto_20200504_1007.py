# Generated by Django 3.0.5 on 2020-05-04 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='customer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='orm.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]