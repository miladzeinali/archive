from django.contrib import admin
from .models import User,Userprofile,Occupation,Corporation

class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','occupation','user')
    search_fields = ('name',)

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CorporationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Userprofile,UserprofileAdmin)
admin.site.register(Occupation,OccupationAdmin)
admin.site.register(Corporation,CorporationAdmin)