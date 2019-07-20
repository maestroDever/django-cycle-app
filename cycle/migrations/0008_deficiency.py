# Generated by Django 2.1.7 on 2019-07-10 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0007_auto_20190621_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('remarks', models.TextField(null=True)),
                ('financials', models.TextField(null=True)),
                ('suggestions', models.TextField(null=True)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycle.Cycle')),
            ],
        ),
    ]