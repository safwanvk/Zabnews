# Generated by Django 3.0.7 on 2020-07-01 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200701_0548'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='link',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='link',
            name='rank_score',
        ),
    ]
