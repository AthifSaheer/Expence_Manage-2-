# Generated by Django 3.1.3 on 2020-12-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0006_remove_addexpense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addamount',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addexpense',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
