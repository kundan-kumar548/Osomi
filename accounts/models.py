from django.db import models
from django.core import validators
from django.contrib.auth.models import User


# Address
class Address(models.Model):
    address = models.CharField(max_length=100, default=None, null=True)
    landmark = models.CharField(max_length=50, default=None, null=True)
    city = models.CharField(max_length=50, default=None, null=True)
    state = models.CharField(max_length=20, default=None, null=True)
    pin = models.IntegerField(default=None, null=True)
    country = models.CharField(max_length=40, default=None, null=True)

    def __str__(self):
        return self.city


# New user signing Up
class UserSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return self.user.email


# Detailed user details
class UsersProfile(models.Model):
    user = models.OneToOneField(UserSignup, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now_add=False, blank=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    website = models.URLField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.user.user.email


# Artists account details
class ArtistAccount(models.Model):
    user = models.OneToOneField(UsersProfile, on_delete=models.CASCADE)
    email2 = models.EmailField(max_length=60)
    ARTIST_TYPE = (
        ("Painters", "Painters"),
        ("Home decorators", "Home decorators"),
        ("Beauty & SPAs", "Beauty & SPAs"),
        ("Other small business","Other small business"),
    )
    specialist_In = models.CharField(max_length=50, choices=ARTIST_TYPE, default="Painters")

    def __str__(self):
        return self.user.user.user.email

