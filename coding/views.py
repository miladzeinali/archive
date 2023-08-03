from django.shortcuts import render
from coding.models import *

zones = Zone.objects.all()

def Home(request):
    return render(request, 'home.html', {'zones': zones})

def AreaView(request, id):
    areas = Area.objects.filter(zone=id)
    context = {
        'areas': areas,
        'zones': zones
    }
    return render(request, 'home.html', context)


def ME(request, id):
    mes = Main_Equipment.objects.filter(area=id).order_by('ME_code')
    areas=[]
    try:
        areas = Area.objects.filter(zone=mes[0].area.zone).order_by('area')
    except:
        pass
    context = {
        'areas': areas,
        'zones': zones,
        'mes': mes,
    }
    return render(request,'home.html',context)

