# Generated by Django 2.1.7 on 2019-06-21 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0004_auto_20190621_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sampling',
            old_name='Client_Name',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='sampling',
            old_name='Cycle_Type',
            new_name='Cycle',
        ),
        migrations.RemoveField(
            model_name='samples',
            name='control_procedures',
        ),
    ]
