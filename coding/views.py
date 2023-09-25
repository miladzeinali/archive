from django.shortcuts import render, redirect
from coding.models import *
from django.http import JsonResponse
from account.models import Userprofile


def CategoryView(request):
    user = request.user
    if user.is_authenticated:
        profile = Userprofile.objects.get(user=user)
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'profile': profile,
        }
        return render(request, 'index2.html', context)
    else:
        return redirect('account:login')


def AddSameLevel(request):
    id = request.POST['id']
    node = Category.objects.get(id=id)
    child = node.get_children().last()
    new = []
    if node.type == 'ME':
        if not child:
            newname = 10000
        else:
            newname = int(child.name) + 10000
        if newname < 100000:
            name = f'0{newname}'
        else:
            name = newname
        new = Category.objects.create(name=name, slug=name, parent=node, type='MED')
    elif node.type == 'MED':
        if not child:
            newname = 100
        else:
            newname = int(child.name) + 100
        if newname >= 100:
            name = newname
        else:
            name = f'0{newname}'
        new = Category.objects.create(name=name, slug=name, parent=node, type='MEDM')
    elif node.type == 'MEDM':
        if not child:
            newname = 1
        else:
            newname = int(child.name) + 1
        if newname >= 10:
            name = newname
        else:
            name = f'0{newname}'
        new = Category.objects.create(name=name, slug=name, parent=node, type='Part')
    return redirect('coding:addingredirect', new.id)


def AddRedirect(request, obj):
    user = request.user
    if user.is_authenticated:
        profile = Userprofile.objects.get(user=user)
        newnode = Category.objects.get(id=obj)
        family = newnode.get_family()
        return render(request, 'newnode.html', {'newnode': newnode, 'categories': family, 'profile': profile})
    else:
        return redirect('account:login')


def Search(request):
    try:
        user = request.user
        if user.is_authenticated:
            query = request.POST['search']
            profile = Userprofile.objects.get(user=user)
            newnode = Category.objects.get(name__contains=query, type='ME')
            family = newnode.get_family()
            return render(request, 'searchresult.html', {'categories': family, 'newnode': newnode, 'profile': profile})
    except:
        return redirect('coding:category')


def get_parent_node(request):
    node_id = request.GET.get('node_id')
    node = Category.objects.get(id=node_id)
    if node.type == 'Part':
        part = node.name
        father = node.parent.parent.parent.parent.parent.parent.name
        zone = node.parent.parent.parent.parent.parent.name
        area = node.parent.parent.parent.parent.name
        me = node.parent.parent.parent.name
        med = node.parent.parent.name
        medm = node.parent.name
        sum = f'0{int(med) + int(medm) + int(part)}'
        context = {'part': part, 'zone': zone, 'area': area,
                   'me': me, 'med': med,
                   'medm': medm, 'sum': sum, 'father': father}
        return JsonResponse(context)
    elif node.type == 'MEDM':
        part = 0
        father = node.parent.parent.parent.parent.parent.name
        zone = node.parent.parent.parent.parent.name
        area = node.parent.parent.parent.name
        me = node.parent.parent.name
        med = node.parent.name
        medm = node.name
        sum = f'0{int(med) + int(medm) + int(part)}'
        context = {'part': part, 'zone': zone, 'area': area,
                   'me': me, 'med': med,
                   'medm': medm, 'sum': sum, 'father': father}
        return JsonResponse(context)


def Caption(request):
    node_id = request.GET.get('node_id')
    node = Category.objects.get(id=node_id)
    parent = node.parent.name
    name = node.name
    type = node.type
    context = {'name': name, 'parent': parent, 'nodeid': node_id, 'type': type}
    return JsonResponse(context)


def UpdateCaption(request):
    user = request.user
    caption = request.POST['caption']
    id = request.POST['id']
    node = Category.objects.get(id=id)
    parent_name = node.parent.name
    node.caption = caption
    if not caption:
        node.caption = None
    node.save()
    profile = Userprofile.objects.get(user=user)
    newnode = Category.objects.get(name__contains=parent_name, type='ME')
    family = newnode.get_family()
    return render(request, 'searchresult.html', {'categories': family,
                                                 'newnode': newnode, 'profile': profile})

def AddingControl(request):
    node_id = request.GET.get('node_id')
    node = Category.objects.get(id=node_id)
    parent = node.parent.name
    name = node.name
    type = node.type
    context = {'name': name, 'parent': parent, 'nodeid': node_id, 'type': type}
    return JsonResponse(context)
