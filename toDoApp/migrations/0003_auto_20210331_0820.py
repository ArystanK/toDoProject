# Generated by Django 3.1.7 on 2021-03-31 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0002_auto_20210331_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
