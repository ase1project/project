# Generated by Django 3.0.2 on 2020-02-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apple',
            name='title',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
