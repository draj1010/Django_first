# Generated by Django 3.0.5 on 2020-04-14 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.TextField()),
                ('task', models.TextField()),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='todo.Userx')),
            ],
        ),
    ]
