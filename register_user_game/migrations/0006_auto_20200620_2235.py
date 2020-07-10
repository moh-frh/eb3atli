# Generated by Django 3.0.7 on 2020-06-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user_game', '0005_auto_20200620_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_game_name', models.CharField(max_length=30)),
                ('environement', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wish_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_game_name', models.CharField(max_length=30)),
                ('environement', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='game',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AddField(
            model_name='user',
            name='my_game',
            field=models.ManyToManyField(to='register_user_game.My_Game'),
        ),
        migrations.AddField(
            model_name='user',
            name='wish_game',
            field=models.ManyToManyField(to='register_user_game.Wish_Game'),
        ),
    ]
