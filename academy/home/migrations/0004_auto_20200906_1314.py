# Generated by Django 2.2.4 on 2020-09-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200906_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
