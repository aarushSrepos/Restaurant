# Generated by Django 5.1.3 on 2024-12-01 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(default='', max_length=50)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('tableNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.tablerecord')),
            ],
        ),
    ]