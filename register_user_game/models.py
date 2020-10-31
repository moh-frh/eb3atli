from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.IntegerField()
    wilaya = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wilaya+" - [ "+self.email+" ]"


class My_games(models.Model):
    ENV = (
        ('Play_Station', 'Play_Station'),
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
    )

    game_name = models.CharField(max_length=30, blank=True, null=True)
    environement = models.CharField(max_length=30, choices=ENV, blank=True, null=True)  # ps/pc/xbox
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.game_name


class Wish_games(models.Model):
    ENV = (
        ('Play_Station', 'Play_Station'),
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
    )

    game_name = models.CharField(max_length=30, blank=True, null=True)
    # environement = models.CharField(max_length=30, choices=ENV, blank=True, null=True) #ps/pc/xbox
    environement = models.CharField(max_length=30, choices=ENV, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.game_name
