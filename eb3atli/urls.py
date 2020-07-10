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

from eb3atli.views import Home, Register, Get_my_games, Get_wish_games, Dashboard, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('login', Login, name='login'),

    path('register', Register, name='register'),
    path('<int:id>/', Register, name='update_game'),

    path('my_games', Get_my_games, name='my_games'),
    path('wish_games', Get_wish_games, name='wish_games'),
    path('dashboard', Dashboard, name='dashboard'),

    # path('<int:id>/', Register, name='update'),

    # path('register_my_game', Register_My_Game, name='register_my_game'),
    # path('register_wish_game', Register_Wish_game, name='register_wish_game'),

]

urlpatterns += staticfiles_urlpatterns()