# Generated by Django 3.1.3 on 2020-12-09 05:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0002_auto_20201209_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='addamount',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CoreApp.incomecat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addexpense',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CoreApp.expensecat'),
            preserve_default=False,
        ),
    ]
