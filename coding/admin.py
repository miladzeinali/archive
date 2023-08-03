from django.contrib import admin
from .models import *

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('zone',)
    search_fields = ('zone',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('area','zone')
    search_fields = ('area',)

class Main_EquipmentAdmin(admin.ModelAdmin):
    list_display = ('ME_code','area')
    search_fields = ('ME_code',)

class Main_Equipment_DeviceAdmin(admin.ModelAdmin):
    list_display = ('Device','main_equipment')
    search_fields = ('Device',)

class MEDMAdmin(admin.ModelAdmin):
    list_display = ('MED_mother','med')
    search_fields = ('MED_mother',)

class PartAdmin(admin.ModelAdmin):
    list_display = ('part','medm')
    search_fields = ('part',)

admin.site.register(Zone,ZoneAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Main_Equipment,Main_EquipmentAdmin)
admin.site.register(Main_Equipment_Device,Main_Equipment_DeviceAdmin)
admin.site.register(MEDM,MEDMAdmin)
admin.site.register(Part,PartAdmin)