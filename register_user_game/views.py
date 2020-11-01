
from django.shortcuts import render, redirect
from register_user_game.forms import UserForm, My_gamesForm, Wish_gamesForm
from register_user_game.models import User, Wish_games
from .models import My_games
from django.contrib.auth import logout

def Home(request):
    ps_count = Wish_games.objects.filter(environement="Play_Station").count() + My_games.objects.filter(environement="Play_Station").count()
    pc_count = Wish_games.objects.filter(environement="PC").count() + My_games.objects.filter(environement="PC").count()
    xbox_count = Wish_games.objects.filter(environement="Xbox").count() + My_games.objects.filter(environement="Xbox").count()

    context = {'title':"home",
               'ps_count': ps_count,
               'pc_count': pc_count,
               'xbox_count': xbox_count}
    return render(request, 'home.html', context)

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        all_user = User.objects.all()

        for user in all_user:
            if email in user.email and password in user.password and email != "" and password != "":
                request.session['user_logged_id'] = user.id
                wish_games = Wish_games.objects.filter(user=request.session.get('user_logged_id'))
                all_my_games = My_games.objects.all()
                # dashboard_games = set(all_my_games) - ( set(all_my_games) - set(wish_games) )
                dashboard_games = set(all_my_games) and set(wish_games)
                user = User.objects.get(id=request.session.get('user_logged_id'))

                context = {'dashboard_games': dashboard_games,
                           'wish_games': wish_games,
                           'all_my_games': all_my_games,
                           'user': user}
                return render(request, 'dashboard.html', context)

    else:
        return render(request, 'login.html')


# and 'btn_register' in request.POST:
def Register(request):
    form = UserForm()

    if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                print("")
                form.save()
            return redirect('login')

    else:
        context={
            'form': form,
        }
        return render(request, "register.html", context)


def Logout(request):
    logout(request)
    return redirect('home')

def Dashboard(request):
    context = {'title':"dashboard"}

    wish_games = Wish_games.objects.filter(user = request.session.get('user_logged_id'))
    all_my_games = My_games.objects.all()
    # dashboard_games = set(all_my_games) - ( set(all_my_games) - set(wish_games) )
    dashboard_games = set(all_my_games) and set(wish_games)
    user = User.objects.get(id=request.session.get('user_logged_id'))

    context = {'dashboard_games': dashboard_games,
               'wish_games': wish_games,
               'all_my_games': all_my_games,
               'user': user}

    return render(request, 'dashboard.html', context)


def My_Games(request):
    # context = {'title':"my games"}
    all_my_games = My_games.objects.filter(user= request.session['user_logged_id'])
    # context = { 'my_games' : My_games.objects.filter(user = request.session.get('user_logged_id') )}
    context = {'all_my_games': all_my_games,
               'user': User.objects.get(id=request.session.get('user_logged_id')),
               }

    return render(request, 'my_games.html', context)
    # return HttpResponse("my games")

def Add_new_my_game(request):
    all_my_games = My_games.objects.all()
    form = My_gamesForm()
    if request.method == "POST":
        form = My_gamesForm(request.POST)
        if form.is_valid():
            user_id = request.session['user_logged_id']

            user = User.objects.get(id=user_id)
            instance = My_games.objects.create(game_name=request.POST.get("game_name"),
                                               environement=request.POST.get("environement"))
            instance.user.add(user)

        return redirect('my_games')
    else:
        context = {
            'form': form,
            'user': request.session.get('user_logged_id'),
        }
        return render(request, "add_my_game.html", context)

    return render(request, 'add_my_game.html', context)

def Update_my_game(request,pk):
    my_games = My_games.objects.get(id=pk)
    form = My_gamesForm(instance=my_games)

    if request.method == 'POST':
        form = My_gamesForm(request.POST, instance=my_games)
        if form.is_valid():
            form.save()
            return redirect("my_games")
        else:
            return redirect("my_games")

    context = {'nom_page': 'gestion des rapports',
               'form': form,
               'user': request.session.get('user_logged_id'),
               }
    return render(request, 'update_my_game.html', context)


def Delete_my_game(request,pk):
    my_games = My_games.objects.get(id=pk)
    my_games.delete()

    return redirect('my_games')


def Wish_Games(request):
    all_wish_games = Wish_games.objects.filter(user=request.session['user_logged_id'])
    # context = { 'my_games' : My_games.objects.filter(user = request.session.get('user_logged_id') )}
    context = {'all_wish_games': all_wish_games,
               'user': User.objects.get(id=request.session.get('user_logged_id')),
               }
    # context = { 'wish_games' : Wish_games.objects.filter(user = request.session.get('user_logged_id') )}
    return render(request, 'wish_games.html', context)

def Add_new_wish_game(request):
    all_my_games = Wish_games.objects.all()
    form = Wish_gamesForm()
    if request.method == "POST":
        form = Wish_gamesForm(request.POST)
        if form.is_valid():
            user_id = request.session['user_logged_id']

            user = User.objects.get(id=user_id)

            instance = Wish_games.objects.create(game_name=request.POST.get("game_name"),
                                               environement=request.POST.get("environement"))

            instance.user.add(user)

        return redirect('wish_games')
    else:
        context = {
            'form': form,
            'user': request.session.get('user_logged_id'),
        }
        return render(request, "add_wish_game.html", context)

    return render(request, 'add_wish_game.html', context)

def Update_wish_game(request,pk):
    wish_games = Wish_games.objects.get(id=pk)
    form = Wish_gamesForm(instance=wish_games)

    if request.method == 'POST':
        form = Wish_gamesForm(request.POST, instance=wish_games)
        if form.is_valid():
            form.save()
            return redirect("wish_games")
        else:
            return redirect("wish_games")

    context = {'nom_page': 'gestion des rapports',
               'form': form,
               'user': request.session.get('user_logged_id'),
               }
    return render(request, 'update_wish_game.html', context)


def Delete_wish_game(request,pk):
    wish_games = Wish_games.objects.get(id=pk)
    wish_games.delete()

    return redirect('wish_games')


def Game_details(request):

    return render(request, 'game_details.html')


def Contact(request):
    context = {'title':"contact"}
    return render(request, 'contact.html', context)

