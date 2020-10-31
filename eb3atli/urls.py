"""eb3atli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from register_user_game.views import Home, Login, Register, Dashboard, Add_new_wish_game, Add_new_my_game, \
    My_Games, Wish_Games, Update_my_game, Delete_my_game, Update_wish_game, Delete_wish_game, Logout, Game_details, \
    Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),

    path('login', Login, name='login'),
    path('register', Register, name='register'),
    path('<int:id>/', Register, name='update_game'),

    path('my_games', My_Games, name='my_games'),
    path('wish_games', Wish_Games, name='wish_games'),

    path('dashboard', Dashboard, name='dashboard'),
    path('contact', Contact, name='contact'),

    path('add_new_wish_game', Add_new_wish_game, name='add_new_wish_game'),
    path('Add_new_my_game', Add_new_my_game, name='add_new_my_game'),

    path('update_my_game/<str:pk>/', Update_my_game, name='update_my_game'),
    path('delete_my_game/<str:pk>/', Delete_my_game, name='delete_my_game'),

    path('update_wish_game/<str:pk>/', Update_wish_game, name='update_wish_game'),
    path('delete_wish_game/<str:pk>/', Delete_wish_game, name='delete_wish_game'),

    path('logout', Logout, name='logout'),

    path('game_details', Game_details, name='game_details'),

    # path('<int:id>/', Register, name='update'),

]

urlpatterns += staticfiles_urlpatterns()