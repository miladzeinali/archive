from django.db import models
from django.contrib.auth.models import User

class Corporation(models.Model):
    name = models.CharField(max_length=60)
    manager = models.OneToOneField(User,on_delete=models.CASCADE,default=1)

class Occupation(models.Model):
    name = models.CharField(max_length=60)
    manager = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    corporation = models.OneToOneField(Corporation,on_delete=models.CASCADE,default=1)

class Userprofile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    TYPE_CHOICE = (
        (1,'superadmin'),
        (2,'admin'),
        (3,'employee'),
        (4,'viewer'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICE,default=4)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    occupation = models.OneToOneField(Occupation,on_delete=models.CASCADE,default=1)
