from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class Director(models.Model):
    first_names = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_names} {self.last_name}"

    def delete_url(self):
        return f'/delete-director/{self.id}'

    def edit_url(self):
        return f'/edit-director/{self.id}'

    def get_films_url(self):
        return f'/by-director/{self.id}'


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    def delete_url(self):
        return f'/delete-genre/{self.id}'

    def edit_url(self):
        return f'/edit-genre/{self.id}'

    def get_films_url(self):
        return f'/by-genre/{self.id}'


class Film(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=256)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    year = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} {self.director} {self.year}"

    def delete_url(self):
        return f'/delete-film/{self.id}'

    def edit_url(self):
        return f"/edit-film/{self.id}"

    def details_url(self):
        return f"/film/{self.id}"


class Comment(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.added_by} {self.content}"

    def delete_url(self):
        return f'/delete-comment/{self.id}'

    def edit_url(self):
        return f"/edit-comment/{self.id}"
