# Generated by Django 3.1.4 on 2021-01-04 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210104_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]