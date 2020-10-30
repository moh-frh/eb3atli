from django import forms
from .models import User, My_games, Wish_games


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__' # or ('name', 'passwoerd',....)

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.fields['game'].empty_label = "select"

class My_gamesForm(forms.ModelForm):

    class Meta:
        model = My_games
        # fields = '__all__' # or ('name', 'passwoerd',....)
        fields = ['game_name', 'environement']

    # def __init__(self, *args, **kwargs):
    #     super(My_gamesForm, self).__init__(*args, **kwargs)
    #     self.fields['environement'].empty_label = "select"
    #
    #     self.fields['game_name'].required = False
    #     self.fields['environement'].required = False

class Wish_gamesForm(forms.ModelForm):

    class Meta:
        model = Wish_games
        fields = ['game_name', 'environement']
        # fields = '__all__' # or ('name', 'passwoerd',....)

    # def __init__(self, *args, **kwargs):
    #     super(Wish_gamesForm, self).__init__(*args, **kwargs)
    #     self.fields['environement'].empty_label = "select"
    #
    #     self.fields['game_name'].required = False
    #     self.fields['environement'].required = False

