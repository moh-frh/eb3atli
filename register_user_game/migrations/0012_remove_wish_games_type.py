# Generated by Django 3.0.7 on 2020-10-24 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_user_game', '0011_auto_20201024_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish_games',
            name='type',
        ),
    ]
