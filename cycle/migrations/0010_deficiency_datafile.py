# Generated by Django 2.1.7 on 2019-07-11 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0009_remove_deficiency_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='deficiency',
            name='datafile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cycle.DatafileModel'),
            preserve_default=False,
        ),
    ]
