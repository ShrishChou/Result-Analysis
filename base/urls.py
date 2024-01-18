from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home,name="home" ),
    path("players/",views.players,name="players"),
    path("profile/<str:pk>/",views.profile,name="profile"),
    path("login/",views.loginPage,name="login"),
    path("duel-form/",views.logDuel,name="duel-form"),
    path("teamstats/",views.duel_list,name="teamstats"),
    path("match-form/",views.logMatch,name="match-form"),
    path("logistics/",views.scrapingtest,name="logistics"),
    path("logout/",views.logoutUser,name="logout"),


]
