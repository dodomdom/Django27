# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-04 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171104_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='classify',
            field=models.CharField(choices=[('\uc7a1\ub2f4', '\uc7a1\ub2f4'), ('\ucef4\ud4e8\ud130', '\ucef4\ud4e8\ud130'), ('\uc601\ud654', '\uc601\ud654'), ('\uac8c\uc784', '\uac8c\uc784'), ('\ub4dc\ub77c\ub9c8', '\ub4dc\ub77c\ub9c8'), ('\ubb38\uc758', '\ubb38\uc758')], default='\uc7a1\ub2f4', max_length=10),
        ),
    ]