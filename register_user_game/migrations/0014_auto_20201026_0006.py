# Generated by Django 3.0.7 on 2020-10-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user_game', '0013_remove_my_games_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish_games',
            name='environement',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]