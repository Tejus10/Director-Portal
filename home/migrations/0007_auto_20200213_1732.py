# Generated by Django 3.0.1 on 2020-02-13 12:02

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200213_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal_letter',
            name='si_no',
            field=models.IntegerField(default=home.models.internal_letter.number),
        ),
    ]
