# Generated by Django 4.0.6 on 2022-11-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Rdate',
            field=models.DateField(),
        ),
    ]
