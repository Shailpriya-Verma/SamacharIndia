# Generated by Django 3.2.8 on 2022-01-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220121_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ncity',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='videonews',
            name='vcity',
            field=models.CharField(max_length=500),
        ),
        migrations.DeleteModel(
            name='city',
        ),
    ]