# Generated by Django 3.1.7 on 2021-03-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]