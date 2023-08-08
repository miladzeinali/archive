from django.shortcuts import render
from coding.models import *

zones = Zone.objects.all()

def Home(request):
    return render(request, 'index2.html', {'zones': zones})

def CategoryView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'index2.html', context)

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

def AddSameLevel(request,id):
    node = Category.objects.get(id=id)
    parent = node.parent.type

