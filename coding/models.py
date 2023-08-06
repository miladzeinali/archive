import datetime
from django.db.models.fields import SlugField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(verbose_name=_("Category safe Url"),max_length=255,unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE, null=True,blank=True,related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertaion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args= [self.slug])
    
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
      verbose_name=_("title"),help_text=_("Required"), max_length=255,
    )

    description = models.TextField(
      verbose_name=_("description"),help_text=_("Not Required"), blank=True 
    )
    slug = SlugField(max_length=255)
    is_active = models.BooleanField(
      verbose_name=_("Product Visibility"),help_text=_("Change Product Visibility"), default=True,  
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True , editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now = True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
       
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






