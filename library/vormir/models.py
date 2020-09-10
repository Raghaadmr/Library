from django.db import models
from django.contrib.auth.models import User
from isbn_field import ISBNField
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.auth.models import AbstractUser
#from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin

# class User(SimpleEmailConfirmationUserMixin, AbstractUser):
#     pass

class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    year_of_release = models.PositiveIntegerField(default=datetime.date.today().year, validators=[MinValueValidator(1100),MaxValueValidator(datetime.date.today().year)])
    isbn = ISBNField(clean_isbn=False)
    genre = models.CharField(max_length=100)
    borrowed = models.BooleanField(default=False)
    cover = models.ImageField(null=True, blank=True)


class Member(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class Library(models.Model):
    librarian = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    members = models.ManyToManyField(Member)

# class Borrowed(models.Model):
#     borrowed = models.BooleanField(default=False)
#     borrowdate = models.PositiveIntegerField(default=datetime.date.today().year, validators=[MinValueValidator(1100),MaxValueValidator(datetime.date.today().year)])
#     whoborrows=models.ForeignKey(Member, default=1, on_delete=models.CASCADE)
