# Generated by Django 2.2.4 on 2020-09-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200906_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='feedback',
            field=models.CharField(default='None', max_length=250),
        ),
    ]
