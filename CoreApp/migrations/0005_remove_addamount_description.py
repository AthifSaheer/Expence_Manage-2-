# Generated by Django 3.1.3 on 2020-12-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0004_auto_20201209_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addamount',
            name='description',
        ),
    ]
