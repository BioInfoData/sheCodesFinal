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
    type = models.CharField(max_length=300, choices = CHOICES_TYPE)
    gender = models.CharField(max_length=300, choices = CHOICES_GENDER)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(blank=True,max_length=20)
    profileimg = models.ImageField(default='defaul_profile.jpg', blank=True) # TODO change the default img in assets


    def __str__(self):
        return str(self.user)

class Details(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userid = models.IntegerField()
    username = models.CharField(max_length=100)
    birth = models.DateField(default=date.today)
    exp = models.IntegerField(default=0) # years of experience

    def __str__(self):
        return str(self.user)

class Connection(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    connected_user = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return str(self.username)

class Reply(models.Model): # babysitter reply messages - only when got reply. To add to Serach
    babysitter = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return str(self.id)

class Search(models.Model):
    username = models.CharField(max_length = 100) #parent username
    min_exp = models.IntegerField()
    gender = models.CharField(max_length=300, choices=CHOICES_GENDER)
    message = models.TextField()
    results = models.ManyToManyField(Details, blank=True) # list of babysitter found with the params
    reply = models.ManyToManyField(Reply, blank=True)  # list of babysitter replys

    def __str__(self):
        return str(self.id)

class ReplySearch(models.Model): # babysitter reply messages all - including no reply
    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    babysitter = models.CharField(max_length = 100)
    parent = models.CharField(max_length=100)
    message = models.TextField(blank=True)


    def __str__(self):
        return str(self.id)