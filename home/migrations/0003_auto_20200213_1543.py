# Generated by Django 3.0.1 on 2020-02-13 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200213_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='external_past',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('fro', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('dated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='internal_past',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('fro', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('dated', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='external_letter',
            name='history',
        ),
        migrations.RemoveField(
            model_name='internal_letter',
            name='history',
        ),
        migrations.DeleteModel(
            name='past',
        ),
        migrations.AddField(
            model_name='internal_past',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.internal_letter'),
        ),
        migrations.AddField(
            model_name='external_past',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.external_letter'),
        ),
    ]
