# Generated by Django 3.0.7 on 2020-06-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user_game', '0006_auto_20200620_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=30)),
                ('environement', models.CharField(choices=[('Play-Station', 'Play-Station'), ('PC', 'PC'), ('Xbox', 'Xbox')], max_length=30)),
                ('type', models.CharField(choices=[('my_games', 'my_games'), ('wish_games', 'wish_games')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='my_game',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wish_game',
        ),
        migrations.DeleteModel(
            name='My_Game',
        ),
        migrations.DeleteModel(
            name='Wish_Game',
        ),
        migrations.AddField(
            model_name='user',
            name='game',
            field=models.ManyToManyField(to='register_user_game.Game'),
        ),
    ]
