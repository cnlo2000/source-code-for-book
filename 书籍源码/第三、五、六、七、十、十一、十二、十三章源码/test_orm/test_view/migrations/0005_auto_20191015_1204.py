# Generated by Django 2.1.4 on 2019-10-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_view', '0004_auto_20190908_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gander',
            field=models.CharField(choices=[('1', '男'), ('2', '女')], max_length=1, verbose_name='性别'),
        ),
    ]
