# Generated by Django 2.1.7 on 2019-06-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0006_auto_20190621_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampling',
            name='Sample_Exception_Rate',
            field=models.IntegerField(null=True),
        ),
    ]
