# Generated by Django 2.1.3 on 2019-09-18 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0022_auto_20190917_1352'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='xmlgraph',
            unique_together={('XMLGraph', 'cycle_in_obj')},
        ),
    ]
