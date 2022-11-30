from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from datetime import date
# Create your models here.

User = get_user_model()

CHOICES_TYPE = (("Parent", "Parent"),
                ("Babysitter", "Babysitter"))
CHOICES_GENDER = (("Male", "Male"),
                  ("Female", "Female"))


# Create your models here.
class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.CharField(max_length = 100)
    userid = models.IntegerField()
    type = models.CharField(max_length=300, choices = CHOICES_TYPE,blank=True)
    gender = models.CharField(max_length=300, choices = CHOICES_GENDER,blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,blank=True)
    phone = models.IntegerField(default=0,blank=True)
    profileimg = models.ImageField(default='defaul_profile.jpg', blank=True) # TODO change the default img in assets


    def __str__(self):
        return str(self.user)

class Details(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userid = models.IntegerField()
    username = models.CharField(max_length=100)
    birth = models.DateField(default=date.today, blank=True)
    exp = models.IntegerField(default=0, blank=True) # years of experience

    def __str__(self):
        return str(self.user)

class Connection(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    connected_user = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return str(self.username)

class Search(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    min_exp = models.IntegerField(default=0, blank=True)
    gender = models.CharField(max_length=300, choices=CHOICES_GENDER, blank=True)

    def __str__(self):
        return str(self.username)