# Generated by Django 2.1.7 on 2019-07-20 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0015_auto_20190720_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafilemodel',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cycle.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datafilemodel',
            name='cycle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cycle.Cycle'),
            preserve_default=False,
        ),
    ]
