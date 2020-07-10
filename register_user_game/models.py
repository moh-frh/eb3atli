from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class My_games(models.Model):

    ENV=(
        ('Play-Station','Play-Station'),
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
    )

    TYPE=(
        ('my_games','my_games'),
        ('wish_games', 'wish_games'),
    )

    game_name = models.CharField(max_length=30, blank=True, null=True)
    environement = models.CharField(max_length=30, choices=ENV, blank=True, null=True) #ps/pc/xbox

    def __str__(self):
        # return "("+self.environement+") "+self.game_name
        return self.game_name

class Wish_games(models.Model):

    ENV=(
        ('Play-Station','Play-Station'),
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
    )

    game_name = models.CharField(max_length=30, blank=True, null=True)
    environement = models.CharField(max_length=30, choices=ENV, blank=True, null=True) #ps/pc/xbox

    def __str__(self):
        # return "(" + self.environement + ") " + self.game_name
        return self.game_name


class User(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.IntegerField()
    wilaya = models.CharField(max_length=30)

    my_games = models.ManyToManyField(My_games)
    wish_games = models.ManyToManyField(Wish_games)

    def __str__(self):
        return self.user_name

