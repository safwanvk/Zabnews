# Generated by Django 3.0.7 on 2020-06-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200630_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='vote_score',
        ),
        migrations.AddField(
            model_name='link',
            name='rank_score',
            field=models.FloatField(default=0.0),
        ),
    ]