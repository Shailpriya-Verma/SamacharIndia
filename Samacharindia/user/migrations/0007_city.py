# Generated by Django 3.2.8 on 2022-01-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_news_ndes'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=300)),
                ('cdate', models.DateField()),
            ],
        ),
    ]
