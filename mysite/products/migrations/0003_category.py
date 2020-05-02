# Generated by Django 3.0.5 on 2020-05-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
            bases=('products.product',),
        ),
    ]
