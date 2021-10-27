"""FilmApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path("", views.menu, name="menu"),
    path('admin/', admin.site.urls),

    path("director/", views.add_director, name="director"),
    path("genre/", views.add_genre, name="genre"),
    path("film/", views.add_film, name="film"),

    path("films/", views.show_films, name="films"),
    path("genres/", views.show_genres, name="genres"),
    path("directors/", views.show_directors, name="directors"),

    path("delete-director/<int:id>", views.delete_director, name="delete_director"),
    path("delete-genre/<int:id>", views.delete_genre, name="delete_genre"),
    path("delete-film/<int:id>", views.delete_film, name="delete_film"),

    path("edit-film/<int:id>", views.edit_film, name="edit_film"),
    path("edit-director/<int:id>", views.edit_director, name="edit_director"),
    path("edit-genre/<int:id>", views.edit_genre, name="edit_genre"),

    path("register/", views.register, name="register"),
    path("login/", views.login_usr, name="login"),
    path("logout/", views.logout_usr, name="logout"),

    path("by-genre/<int:id>", views.genre_film, name="by_genre"),
    path("by-director/<int:id>", views.director_film, name="by_director"),
    path("film/<int:id>", views.film_details, name="film_details")

]
