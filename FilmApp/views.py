from django.shortcuts import redirect, render
from .models import Director, Genre, Film, User, Comment
from .forms import FilmForm, GenreForm, DirectorForm, CustomUserCreationForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def menu(request):
    if request.method == "GET":
        return render(request, "base.html")


@login_required(login_url="login")
def add_director(request):
    form = DirectorForm(request.POST)
    if request.method == "GET":
        return render(request, "object.html", {"form": form})
    else:
        if form.is_valid():
            form.save()
        return redirect("/")


@login_required(login_url="login")
def add_genre(request):
    form = GenreForm(request.POST)
    if request.method == "GET":
        return render(request, "object.html", {"form": form})
    else:
        if form.is_valid():
            form.save()
        return redirect("/")


@login_required(login_url="login")
def add_film(request):
    form = FilmForm(request.POST)
    if request.method == "GET":
        return render(request, "object.html", {"form": form})
    else:
        if form.is_valid():
            added_by = request.user
            name = form.cleaned_data["name"]
            director = form.cleaned_data["director"]
            year = form.cleaned_data["year"]
            genre = form.cleaned_data["genre"]
            description = form.cleaned_data["description"]
            Film.objects.create(added_by=added_by, name=name, director=director,
                                year=year, genre=genre, description=description)
            messages.info(request, f"Film {name} added")
        return redirect("/")


def show_films(request):
    films = Film.objects.all()
    if request.method == "GET":
        return render(request, "films_list.html", {'object_list': films})


def show_genres(request):
    genres = Genre.objects.all()
    if request.method == "GET":
        return render(request, "genre_director.html", {"object_list": genres})


def show_directors(request):
    directors = Director.objects.all()
    if request.method == "GET":
        return render(request, "genre_director.html", {"object_list": directors})


@login_required(login_url="login")
def delete_director(request, id):
    director = Director.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "delete_object.html", {"obj": director})
    else:
        if request.POST['submit'] == "YES":
            director.delete()
            return redirect("/directors")
        else:
            return redirect("/directors")


@login_required(login_url="login")
def delete_genre(request, id):
    genre = Genre.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "delete_object.html", {"obj": genre})
    else:
        if request.POST['submit'] == "YES":
            genre.delete()
            return redirect("/genres")
        else:
            return redirect("/genres")


@login_required(login_url="login")
def delete_film(request, id):
    film = Film.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "delete_object.html", {"obj": film})
    else:
        if request.POST['submit'] == "YES":
            film.delete()
            return redirect("/films")
        else:
            return redirect("/films")


@login_required(login_url="login")
def edit_film(request, id):
    film = Film.objects.get(pk=id)
    form = FilmForm(instance=film)
    if request.method == "GET":
        return render(request, "edit_object.html", {"object": film, "form": form})
    else:
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
        return redirect("/films/")


@login_required(login_url="login")
def edit_director(request, id):
    director = Director.objects.get(pk=id)
    form = DirectorForm(instance=director)
    if request.method == "GET":
        return render(request, "edit_object.html", {"object": director, "form": form})
    else:
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
        return redirect("/directors/")


@login_required(login_url="login")
def edit_genre(request, id):
    genre = Genre.objects.get(pk=id)
    form = GenreForm(instance=genre)
    if request.method == "GET":
        return render(request, "edit_object.html", {"object": genre, "form": form})
    else:
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
        return redirect("/genres/")


def register(request):
    if request.user.is_authenticated:
        return redirect("menu")
    else:
        form = CustomUserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("register")
        return render(request, "object.html", {"form": form})


def login_usr(request):
    if request.user.is_authenticated:
        return redirect("menu")
    else:
        if request.method == "POST":
            usr = request.POST.get("username")
            pwd = request.POST.get("password")
            user = authenticate(request, username=usr, password=pwd)
            if user is not None:
                login(request, user)
                return redirect("menu")
            else:
                messages.info(request, "Username or password incorrect")
        return render(request, "login.html")


@login_required(login_url="login")
def logout_usr(request):
    logout(request)
    return redirect("menu")


def genre_film(request, id):
    genre = Genre.objects.get(pk=id)
    films = Film.objects.filter(genre=genre)
    if request.method == "GET":
        return render(request, "films_list.html", {"object_list": films})


def director_film(request, id):
    director = Director.objects.get(pk=id)
    films = Film.objects.filter(director=director)
    if request.method == "GET":
        return render(request, "films_list.html", {"object_list": films})


@login_required(login_url="login")
def film_details(request, id):
    film = Film.objects.get(pk=id)
    comments = Comment.objects.filter(film=film)
    form = CommentForm()
    if request.method == "GET":
        return render(request, "film_details.html", {"film": film, "comments": comments, "form": form})
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            added_by = request.user
            film = film
            content = form.cleaned_data["content"]
            Comment.objects.create(added_by=added_by, film=film, content=content)
        else:
            messages.info(request, "Something wrong with the comment")
        return render(request, "film_details.html", {"film": film, "comments": comments, "form": form})
