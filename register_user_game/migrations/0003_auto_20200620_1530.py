# Generated by Django 3.0.7 on 2020-06-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user_game', '0002_auto_20200620_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='game',
        ),
        migrations.AlterField(
            model_name='game',
            name='environement',
            field=models.CharField(choices=[('Play-Station', 'Play-Station'), ('PC', 'PC'), ('Xbox', 'Xbox')], max_length=30),
        ),
        migrations.AlterField(
            model_name='game',
            name='type',
            field=models.CharField(choices=[('my_games', 'my_games'), ('wish_games', 'wish_games')], max_length=30),
        ),
    ]
