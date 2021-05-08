# Generated by Django 3.1.5 on 2021-05-08 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210104_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='belief',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='computer',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='english',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='sum',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='arabic',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='art',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='math',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='science',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]