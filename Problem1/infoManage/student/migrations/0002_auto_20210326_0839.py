# Generated by Django 3.1.2 on 2021-03-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='roll',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
