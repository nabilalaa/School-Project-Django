# Generated by Django 3.1.4 on 2021-01-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210104_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]