import datetime

from django.db import models
from django.contrib.auth.models import User


class Zone(models.Model):
    zone = models.PositiveSmallIntegerField(default=100)
    def __str__(self):
        return str(self.zone)

class Area(models.Model):
    area = models.PositiveSmallIntegerField(default=150)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.area)

class Main_Equipment(models.Model):
    ME_code = models.CharField(max_length=15)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.ME_code

class Main_Equipment_Device(models.Model):
    Device = models.CharField(max_length=20,default='i3ch')
    main_equipment = models.ForeignKey(Main_Equipment,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.Device

class MEDM(models.Model):
    MED_mother = models.CharField(max_length=25,default='i3ch')
    med = models.ForeignKey(Main_Equipment_Device,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.MED_mother

class Part(models.Model):
    part = models.CharField(max_length=30,default='i3ch')
    medm = models.ForeignKey(MEDM,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.part






