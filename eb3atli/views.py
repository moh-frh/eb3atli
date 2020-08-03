from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from register_user_game.forms import UserForm, MyGamesForm, WishGamesForm
from register_user_game.models import My_games, Wish_games, User


def Home(request):
    context = {'title':"home"}
    return render(request, 'home.html', context)

def Login(request):
    context = {'title':"login"}

    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        for user in User.objects.all():
            if username in user.email and password in user.password:
                request.session['user_logged_id'] = user.id
                return render(request, 'dashboard.html')

        return render(request, 'login.html',context )

    # if request.user.is_authenticated:
    #     return redirect('home')
    #
    # else:
    #     if request.method == 'POST':
    #         username = request.POST.get('email')
    #         password = request.POST.get('password')
    #
    #         user = authenticate(request, username=username, password=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             return redirect('home')
    #         else:
    #             messages.info(request, "username or password incorrect !")
    #
    #     return render(request, 'login.html')


def Register(request, id=0):

    if request.method == "GET":
            if id == 0:
                form = UserForm()
                add_new_games = MyGamesForm()
            else:
                game = My_games.objects.get(pk=id)
                form = UserForm(instance=game)

            return render(request, "register.html", {'title':"register", 'form': form, 'add_new_games': add_new_games})

    if request.method == "POST" and 'btn_register' in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')


    if request.method == "POST" and 'btn_add_new_game' in request.POST:
            add_new_games = MyGamesForm(request.POST)
            add_new_games2 = WishGamesForm(request.POST)

            if add_new_games.is_valid():
                add_new_games.save()
                add_new_games2.save()
            return redirect('register')




def Add_new_game(request):
    context = {'my_games': My_games.objects.filter(user=3)}
    return render(request, 'my_games.html', context)



def Get_my_games(request):
    context = {'title':"my games"}

    context = { 'my_games' : My_games.objects.filter(user = request.session.get('user_logged_id'))}
    return render(request, 'my_games.html', context)

def Get_wish_games(request):
    context = {'title':"wish games"}

    context = { 'wish_games' : Wish_games.objects.filter(user = request.session.get('user_logged_id') )}
    return render(request, 'wish_games.html', context)

def Dashboard(request):
    context = {'title':"dashboard"}

    wish_games = Wish_games.objects.filter(user = request.session.get('user_logged_id'))
    all_my_games = My_games.objects.all()
    # tmp = set(all_my_games) - set(wish_games)
    # dashboard_games = set(all_my_games) - ( set(all_my_games) - set(wish_games) )
    dashboard_games = set(all_my_games) & set(wish_games)

    context = {'dashboard_games' : dashboard_games, 'wish_games':wish_games, 'all_my_games':all_my_games }


    return render(request, 'dashboard.html', context)

def Contact(request):
    context = {'title':"contact"}
    return render(request, 'contact.html', context)

