# Generated by Django 2.1.7 on 2019-07-11 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0008_deficiency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deficiency',
            name='number',
        ),
    ]
